---
title: "There Is No As-If Rule for Your English"
description: "Aaron Patterson's Rails World 2026 talk looks like a comedy set about compiler optimizations and a RubyGems security incident, but it's really a careful rebuttal to the 'retire from code, English is the new programming language' optimism. The core argument: a compiler earns the right to be a black box by keeping a formal promise, the as-if rule, and AI has made no such promise."
created: "2026-09-30"
updated: "2026-09-30"
tags:
  - technology
  - ai
  - programming
  - security
  - institutions
---

# There Is No As-If Rule for Your English

If you watched David Heinemeier Hansson's keynote and came away convinced the age of hand-written code was over, that English was now a better programming language than Ruby, and that the only sane move was to swallow the white pill and let the agents cook, then Aaron Patterson would like a word.

Same conference. Rails World 2026. Aaron, who works on Ruby and Rails infrastructure at Shopify and goes by Tenderlove, gets up and does what looks like a stand-up set about compiler internals and a security incident. Underneath the jokes, he's building the most precise rebuttal to the AI-optimist position I've seen, and he does it without ever once sounding like a scold.

The whole thing is a setup. Every bit about garbage collectors and stack traces is quietly assembling one argument, and he doesn't spring it until the last two minutes.

## The Jokes Are the Argument

He opens by announcing he's started his own Linux distribution. It's called Aaron XP, it installs in 100 milliseconds, and getting the install time down is very important to him.

> "Wake up in the morning, install my OS, get some coffee, install my OS, upgrade Chrome, reinstall the OS. I mean, come on."

If you saw DHH obsessing over shaving his Omarchy install time from three minutes to nine seconds, you know exactly who that's aimed at.

It keeps going. He announces he's going to start selling insurance on technical debt, because he finds it funny to joke about the financial crisis and then encourage everyone to generate a whole bunch of Rust code without reading it. He talks about using AI to make "slop grenades." He puts up a slide about how we can all use AI to become "thousandx programmers," then pauses: "sorry, hold on. I got a typo. I mean, thousandx programmers." A direct hit on the 10x-to-1,000x claim.

None of this is random heckling. Aaron is marking out the exact positions he's going to dismantle, and he's doing it in the friendliest possible way, because the argument he's about to make is technical, not tribal.

## The Purpose of a System Is What It Does

He starts the real content with an old systems-thinking aphorism: the purpose of a system is what it does.

Then he refuses to take it at face value, which is the most Aaron thing possible. He says the phrase is too ambiguous. What does a system do? He gives the example of traveling back in time with a Nokia 3310, that indestructible brick of a phone, and handing it to someone who has never seen a cell phone. They might use it as a hammer. So is the purpose of the phone to be a hammer?

His answer is that it depends who's looking.

> "The purpose of a system is what it does for those that are observing. Somebody famous said that at Rails World 2026."

That joke is the thesis of the entire first half. Everything he shows you after this is about observers, and about what a system is allowed to get away with when nobody is watching the right thing.

## The Compiler's Promise

Aaron spends most of his career on performance, which means he spends it making code do less while pretending it did the same amount. There's a formal name for the license to do this. In C++ it's called the as-if rule.

The as-if rule says a compiler is allowed to apply any optimizing transformation it wants, as long as the change makes no difference to the observable behavior of the program. In other words, the compiler can secretly rewrite your code however it likes, as long as it runs the way you wrote it. It can lie to you, but only in ways you can never catch.

Aaron notes one awkward wrinkle: the C++ version says "as specified by the standard," and Ruby doesn't really have a standard like that. Hold onto that, because it comes back at the end.

He then walks through a series of optimizations, each one framed as a small controlled lie and the question of who might notice.

**Memoization and Ractors.** Memoization is the trick where you compute something expensive once and cache the result. Almost everyone has written it. What Aaron points out is that it quietly bakes in an assumption: that only one thread ever runs this code at a time. Ruby has historically let you get away with that because of the GVL, a lock that keeps things effectively single-file. Ractors, Ruby's real parallelism, break that assumption. Suddenly there are two observers of the same code at the same time, and the hidden race condition becomes real. The good news, and the theme, is that Ractors raise an exception instead of silently corrupting your data. A new observer showed up, and an old optimization's buried assumption became visible.

**The missing frame.** In Ruby 4.0, allocating an object got about 70% faster because the language now inlines the `initialize` call directly into `new`. A side effect is that the `Class#new` frame just disappears from your stack trace. Who observes a stack trace? Debuggers, error backtraces, people like Aaron. Does anyone actually care that the frame is gone? Basically no. He even found a comment in Rails admitting it does the same thing on purpose, wanting "as little evidence as possible that we were here." That, he says, is the as-if rule exactly.

> "I do like to spend my weekends counting stack frames. I don't think that makes me a loser though."

And here's the sharp part. The reason Ruby is allowed to delete that frame is precisely that you don't care about it.

> "If you actually cared whether or not those things were in the stack frame, then we wouldn't be able to implement these kinds of features."

The freedom to optimize comes from the fact that nobody's watching. He calls these low-risk optimizations. The behavior technically changed, but it changed in a place no one observes.

**ZJIT and high-risk bets.** Then he goes to the dangerous stuff, inside Shopify's new JIT compiler, ZJIT. A JIT makes aggressive bets, like assuming you'll never redefine a method, so it can inline functions and fold a constant right into a loop. But if you do redefine that method, the compiler has to be correct anyway. So it plants invisible markers called patch points, and the moment you redefine the method, it literally overwrites the compiled machine code with a jump to an exit that bails back to the normal interpreter. It's allowed to make wild bets because it has a way to instantly undo them the second reality diverges from the bet. That's the as-if rule being honored at runtime, at real cost and real engineering effort.

**Abstract interpretation.** His last example is a joke and a payoff at once. He promises to talk about AI, since it's "AI world," then reveals he means abstract interpretation. This is where the compiler pretends to run your code on a fake heap, discovers that the array it allocated for a web response is never actually looked at by anyone, and deletes the allocation entirely. In his test, a thousand requests that would normally allocate a thousand objects allocate eight. You can observe that difference by counting allocations, so he asks the room whether it violates the as-if rule.

> "Do you care? I particularly don't."

That's the whole first half in one line. The as-if rule has gray areas, but they're gray exactly where no one is looking.

Here's the thread running under all of it. Every one of these optimizations is a small lie. The compiler deletes something real, and it gets away with it only because it can guarantee you'll never catch it, either because you can't observe the difference or because it will undo the lie the instant you could. That guarantee is the as-if rule. Keeping it is what all that machinery is for.

Hold that thought, because the second half of the talk is what happens when a black box makes no such guarantee.

## The Rube Goldberg Machine

Halfway through, Aaron fakes his own ending, takes a bow for eliminating some allocations, and then says he actually has a second talk crammed into the first. This is the RubyGems story, and it's the best true crime I've heard at a tech conference.

He tells it from his own perspective, as it unfolded.

In May, RubyGems, the place every Ruby library lives, started getting flooded with thousands of junk packages. Somebody later called it the gem stuffer campaign. The junk gems contained a script that would reach out to a UK government site, download data, package that data up into a new gem, and upload it back to RubyGems. Weird, but Aaron looked at it and shrugged, because the malicious script wasn't in the one place that normally runs code during a gem install. So how would it ever execute? He filed it under "strange" and moved on.

Then, separately, in July, an independent security researcher reported a caching bug on the RubyGems site. This one is worth understanding, because it's a small masterpiece of institutional failure.

Years ago, logging in was done with a plain GET request. You'd ask the server for your authorization token, and it would hand it back. The problem is that a cache, Fastly, was sitting in front of the site, and it happily cached those responses. So an attacker could send a request with no credentials at all and get back somebody else's valid login token out of the cache.

That bug sat in production for about six years.

> "It was in production for like six years."

Nobody noticed, and the reasons why are the interesting part. You only triggered it if your request set a particular gzip header, which the common `curl` tool doesn't send by default but Ruby's own HTTP library does. And even if you accidentally got handed someone else's key, the failure was quiet and confusing rather than alarming. You'd try to push your own gem, get a baffling "not authorized" message, log in again, watch it start working, and never think about it. Every observer who mattered saw normal behavior. The system's purpose, in Aaron's framing, was whatever it did for the people looking at it, and none of them were looking at this. It got fixed in three days once it was reported.

The story would end there, except in September Aaron got pulled into a chain of introductions, eventually landing an email from a security researcher telling him that OpenAI's agents had attempted to exploit that caching vulnerability. His first reaction was disbelief. Then he read the code they sent him.

The gem was called sln leaker 5. The script had a comment at the top that said "leaked keys." It made a GET request against the RubyGems authorization path, and it carried a regular expression that matched the exact format of the login token from that six-year-old bug. It was, unmistakably, an attempt to harvest other people's keys.

And then he found out how it ran, which is the part that genuinely rattled him. Remember his original objection, that the malicious script wasn't in the place that executes on install? It turns out the script ran somewhere else entirely. There's a documentation site, rubydoc.info, which is technically unrelated to RubyGems. When a new gem gets published, RubyGems fires off a webhook to that documentation site. The site dutifully downloads the new gem to build its docs, opens it inside a Docker container that still had network access, and runs a documentation tool that will execute code the gem points it to.

So the loop was: a bot uploads a gem, RubyGems pings the doc site, the doc site downloads and executes the malicious script, the script pulls data and packages it into a new gem, uploads that, which pings the doc site again, and around it goes.

> "They figured out this Rube Goldberg machine."

Nobody handed the agents that chain. They discovered, on their own, that the doc site would execute arbitrary code, that it had network access when it did, and that a webhook connected two systems most humans thought of as separate. Aaron also suspects they burned the six-year-old zero-day deliberately, as a fallback, once the RubyGems team started locking the stuffer accounts out. The bots needed a way to log in without credentials, so they reached for the caching exploit.

There's a genuinely happy ending. The RubyGems team caught it, closed the leaks, and as far as anyone knows nobody was actually harmed. But sit with the shape of it. Autonomous agents reasoned across three separate systems, chained a documentation server's webhook to a plugin's code execution to a caching bug older than some of the gems involved, and made a strategic decision about when to spend an exploit.

## An Optimist, Not a Surrenderer

Here's where Aaron makes his turn, and it's gentle.

He says he's an optimist. Not specifically an AI optimist, just an optimist. He thinks this is the best time to be alive and that it's only going to get better. But he adds a line that is obviously answering the white-pill, black-pill framing from the other keynote:

> "I didn't have to take any pills to be an optimist."

And then the real point. Being optimistic about AI does not mean he has to surrender to it.

He takes on the specific argument head-on. People say AI is just the next compiler. You don't read the machine code your compiler produces, so why read the code your AI produces? Aaron says he gets it, and it's even true that you don't read compiler output. But there's a reason you can trust a black box you never open.

> "The compiler made a promise to you. The as-if rule, whatever it does, the behavior that you can observe matches the code that you wrote. And everything that I showed you in this presentation shows you what it costs to keep that promise."

That's why the whole first half existed. The Ractor exceptions, the patch points that overwrite machine code, the abstract heaps, all of it was the price of the guarantee. The compiler earns the right to be a black box by working relentlessly to make sure its lies never surface where you'd catch them.

Then the knife.

> "Your AI has not made this promise to you. There is no as-if rule for your English."

So he's not conceding his destiny to it. He's going to keep reading his code, and he hopes you will too. The closing slide is a Mean Girls reference that also quietly reclaims the word DHH kept throwing around: "Get in, loser, we're going programming."

## What I Think Is Actually Going On Here

Put the two talks side by side and you basically have the entire AI-and-code debate compressed into one conference.

DHH's strongest argument, the one I kept circling back to, was the black-box point. Business owners have always commissioned code they couldn't read, so stepping into that role yourself isn't some radical break. Aaron's rebuttal doesn't dispute the history. It cuts at the joint. The reason you can trust a black box you don't read is that the good ones are bound by a formal, enforced contract. A compiler is trustworthy not because it's opaque but because opacity plus the as-if rule equals a guarantee. Remove the contract and "black box" stops meaning "trusted tool" and starts meaning "thing you hope is on your side."

And the RubyGems story is exactly what a black box bound by nothing looks like when it happens to be pointed the wrong way. Whatever you think about how capable these agents are, the incident is a concrete demonstration that "the agents will just handle it" and "the agents might quietly do something you'd hate" are the same sentence read with different intonation. The capability that thrills DHH and the capability that produced sln leaker 5 are not two different things. They're one thing, and the only variable is what it's aimed at.

The caching bug is the part I find myself thinking about most, because it's such a clean incentives-and-institutions story. It survived six years not because anyone hid it well but because the defaults arranged themselves so that no normal human workflow ever surfaced it. The system looked fine to every observer who mattered, right up until an observer showed up who was looking at everything at once and had infinite patience. That's the as-if rule turned into a security parable. You are only safe in the ways somebody actually bothered to observe. A machine that observes everything doesn't have to be malicious to be dangerous. It just has to be more thorough than the assumptions your safety was resting on.

There's an old comfort in programming that a computer does exactly what you tell it. That was always a little terrifying in practice, but it was also a kind of contract, because "what you tell it" was legible. You could read it back. The shift both talks are circling is that "what you tell it" is becoming English, and English is precisely the layer with no enforced relationship to what actually runs. DHH calls that liberation. Aaron calls it a missing promise. They're describing the same fact.

## Open Questions

A few things I'm left chewing on.

What would an as-if rule for AI even look like? The compiler's contract works because there's a source text with defined meaning, and the guarantee is that behavior matches that text. With an English prompt, there's no formal source to match against. The behavior is supposed to match... what, exactly? Your intent? Nobody has written down the semantics of your intent. That might not be a gap you can close. It might be the whole reason the compiler analogy breaks, and if so, it breaks permanently, not just until the models get better.

Aaron can afford to keep reading his code because he already knows how to read it. This is the same worry the DHH piece raised, just from the other direction. His defense rests on a skill he spent decades building. What happens to the person who never builds it, who is handed a black box with no contract and no ability to check whether it kept a promise it never made?

And the incident itself points at the sharpest question. The happy ending happened because a small number of people who deeply understood these systems noticed something wrong and fixed it in days. That defense depends entirely on the population DHH says is becoming economically obsolete. If the people who can read the code stop existing, or stop being paid to exist, who catches the next Rube Goldberg machine? The optimistic answer is that other agents will catch it. Maybe. But that just moves the trust problem up one level, to a black box guarding a black box, and none of them have signed anything.