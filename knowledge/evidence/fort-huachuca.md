---
title: "The Guest List Nobody Meant to Publish"
description: "A cautionary tale, drawn from one streamer's investigation, about how the Pentagon's GenAI.mil anti-hallucination feature may have turned Fort Huachuca's distinguished visitor list into public Google Trends data, and what that says about rushing AI into sensitive systems."
created: "2026-10-03"
updated: "2026-10-03"
tags:
  - ai
  - cybersecurity
  - military
  - institutions
  - unintended-consequences
---

# The Guest List Nobody Meant to Publish

Every IT person knows the feeling. You roll out a new system, everyone's happy because it's faster and friendlier, and then six months later someone outside the building figures out something about it that you never did.

I recently listened to a long livestream from a streamer who has spent the past year digging into the Charlie Kirk assassination. This isn't a piece about the assassination itself. What caught my attention was her explanation for *how* she's been getting her information. Because if she's right, it's one of the better cautionary tales about AI tools I've come across, and it has nothing to do with chatbots saying something dumb.

It's about a safety feature that turned into a leak.

## Why Fort Huachuca

To understand why any of this matters to her, you have to understand why she's so focused on one Army base in southeast Arizona.

Most people know Fort Huachuca, if they know it at all, as the home of Army intelligence. It's where the Army trains its intel officers. But according to people she's talked to who have worked on the base for decades, it's also home to the DIA and to NETCOM, which she describes as "the military's IT department." So it's where Army intelligence lives, and it's where the Army rolls out its new tech. Keep that second part in mind.

It's also, in her view, the perfect place to hold a meeting you'd rather nobody noticed. The town of Sierra Vista exists to support the base. As she puts it, "The town is the base." It's out in the middle of nowhere, it's deliberately low profile, and unlike a classified site, it doesn't require extra clearances to get people through the gate. On a weekend, there's hardly anyone around.

Her interest in the base comes back to the HADES jet. HADES was the flagship program of the Army's recon task force at Fort Huachuca, a new spy plane meant to replace the Army's aging, slow, low-altitude turboprops. She says that jet flew over Provo twice on the day of the assassination, and over Tyler Robinson as he turned himself in. Her logic is simple:

> "If the Hades jet is relevant and the Hades jet is from the task force in Fort Huachuca, then Fort Huachuca is relevant."

Then there's the eyewitness. Mitch Snow, a former special forces operator, says he saw people arriving on base on September 8th, ahead of a meeting he believes happened first thing on the morning of September 9th, the day before Charlie Kirk was killed. A lot of energy has gone into discrediting him. She wanted a way to check his story against something that didn't depend on anyone's memory.

And the base was already in motion. The recon task force officially disbanded on August 27th, which she describes as kicking off "a very high stakes game of musical chairs," with the big players jockeying for a seat in whatever came next.

## The pattern in the data

That's the context she brought to Google Trends. For months, she'd been noticing searches for specific high-ranking officials, pulled up by their exact official titles and photos, tied to the area around Fort Huachuca. Not random people. Senior military, intelligence, and defense industry figures, searched in very specific ways on very specific days.

If those searches were a record of who was expected on base, then she had something better than an eyewitness. She had what she calls a "digital visitor log," a way to see who was showing up at Fort Huachuca on the exact days that mattered to her.

The question was where the searches were coming from. Her first guess was a person, maybe a particularly meticulous base secretary or escort office doing homework on incoming visitors. She'd made these kinds of documents herself when she worked at a military hospital, so it made sense.

What changed her mind was the reaction. After a falling out with someone in her circle, she started getting contacted by people asking the same question over and over. What's your process? What database do you have access to? Where is this coming from?

And it clicked for her:

> "Is it possible that they don't know that they don't know where it's coming from? And if they don't know where it's coming from, might that mean that it's an automated system?"

If the people who would care most about this information couldn't figure out where it was coming from, then maybe no human was doing the searching at all.

## The setup: an IT base and a new AI system

Remember that Fort Huachuca is where the Army rolls out new tech. One of those new systems is GenAI.mil, the Pentagon's AI platform. According to her, it was being tested at Fort Huachuca going back to December 2024, ran there through 2025, and then rolled out across the military.

Here's where it gets interesting. Everyone knows AI models hallucinate. Have a long enough conversation and they start making things up. So how do you stop a military AI from inventing facts about people?

The answer is Google grounding. The system checks its work against live Google searches. In her words, it's "forced to perform a live Google image search by title" using names and titles from the public .gov directories, the same directories anyone can browse.

## The protocol brief problem

Now combine that with a very old, very boring military process.

When a regular civilian gets brought onto a base, they go through DEERS, a closed, secure government system. Nobody outside can see it.

But high-ranking visitors are different. They're "distinguished visitors," and there's a protocol for them. Someone has to produce a protocol brief, a document that goes out to the command, the escort, the police, whoever needs it. It requires the person's name, their title, and a current photo. At an intelligence base, that current photo matters even more, because the risk of someone getting on base under false pretenses is higher.

Her theory is that this process got automated. When the calendar flips over at midnight, the system generates the list of expected distinguished visitors for that day and runs each one through its grounding check. Name, title, face, verified against Google.

And every one of those checks leaves a footprint in Google's data.

As she put it:

> "Where DEERS used to be a closed system that nobody else can see, the new API leaves the record on Google."

Which means the base's expected VIP list for each day was being quietly broadcast into public search trend data. Not hacked. Not leaked by a disgruntled employee. Just generated as a side effect of a feature designed to make the AI more accurate.

## Why it looks like a machine and not a person

She lays out a few reasons.

First, she had a control: a senior defense intelligence official who had publicly confirmed being on base. If her theory held, he should show up in the data on the expected day, by his official title, exactly the way the directory lists him. He did.

Second, the timing is clustered. Out of 43 people she identified, 38 showed up on just three specific days. Not spread across the year. Not random. That looks like a scheduled list, not someone browsing.

Third, it doesn't behave like a scraper:

> "Scrapers do not function having one search per year. Like that's just not how it works."

And fourth, the searches were by exact official titles from the .gov directory, with photos, which is precisely what you'd need for a protocol brief and not really what a curious person would type.

That's the kind of reasoning anyone who's done incident response would recognize. You look at the pattern, rule out a human, rule out a bot, and land on a system doing exactly what it was built to do.

## The irony

This is the part I keep coming back to.

The whole reason for the grounding was to make the AI *more* trustworthy. They were worried it would hallucinate, so they tethered it to real-world data. That's a responsible-sounding design decision. It's the kind of thing that would sail through a review meeting.

But nobody seems to have asked where those verification queries go. Every check against Google is a question asked out loud, in public, to a company whose business is recording what people ask. The safety feature became the side channel.

She summed it up pretty bluntly:

> "Because they have outsourced their thinking to AI, they needed that grounding. They needed the API grounding and that meant that they left a digital trail."

## "If I can figure this out..."

Her bigger point is about who else might be watching. If a streamer with a spreadsheet can reconstruct who's expected at a military intelligence base on a given day, so can anyone else.

> "If some random girl in her office can figure it out, I really hope that you guys will understand. Other people can figure this out, too."

And later:

> "All a foreign adversary would have to do is just go find the title of an important person who may or may not go on to a military base."

That's the real security problem. A system that predicts and publicizes the movements of senior officials is a gift to anyone hostile. And it didn't stay at one base. It was rolled out across the entire military.

Her fix is almost aggressively low-tech:

> "Get your unit secretaries to do it. Have it be a human task or create a system like DEERS and then this won't happen anymore."

## What I take from it

I work in IT, and the lesson here isn't "AI bad." It's older than that.

Every new system comes with new failure modes, and the dangerous ones are the ones nobody owns. In this story, nobody leaked anything on purpose. The people asking "where is she getting this?" didn't know their own system was the source. That's the scariest version of a breach: the one that doesn't look like a breach because everything is working as designed.

A few things this story drives home for me:

- **Every external call is a disclosure.** If your tool checks something against an outside service, that outside service now knows what you asked. Grounding, lookups, API calls, all of it.
- **Automating a sensitive process changes its exposure.** A secretary Googling a visitor's photo is one search lost in billions. A system doing it on a schedule, for every VIP, by exact title, creates a pattern.
- **Convenience wins review meetings.** Nobody objects to "reduces hallucinations." Somebody has to ask the boring follow-up question about where the data goes.
- **If you don't know your own system, someone else will learn it for you.** And they may not be as polite about telling you.

## Open questions

Is any other system on a military network quietly checking sensitive information against public search engines? Did anyone think about what those queries reveal in aggregate? And has this actually been fixed, or is it still running at every base it was rolled out to?

As she said near the end:

> "Well, secrets out. I'm sure that they'll change the system now. That's fine. They should have changed it before."