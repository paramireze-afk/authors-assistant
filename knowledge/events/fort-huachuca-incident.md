---
title: "The Guest List Nobody Meant to Publish"
description: "How researchers claim an automated AI lookup system at Fort Huachuca left a trail in Google Trends, appearing to show who was expected on base in the weeks before Charlie Kirk's assassination, and where that theory still doesn't quite add up."
created: "2026-10-02"
updated: "2026-10-02"
tags:
  - fort-huachuca
  - charlie-kirk
  - google-trends
  - artificial-intelligence
  - intelligence-agencies
---

# The Guest List Nobody Meant to Publish

Most leaks need a leaker. Somebody copies a file, walks out with a thumb drive, or calls a reporter.

This one, if the theory holds, needed something much more boring. An AI system that was told not to make things up.

## The base

Fort Huachuca sits in the high desert of southern Arizona, about fifteen miles from the Mexican border, right up against the town of Sierra Vista. Most people have never heard of it, which is kind of the point.

It's the home of Army military intelligence. It's where the Army trains its intelligence soldiers. It's also home to NETCOM, which is basically the Army's IT department, and the Electronic Proving Ground, where the Army tests new electronics and communications gear before it goes out to the force.

So if you wanted a place where the military's intelligence world and its newest technology overlap, this is pretty much it.

## The allegation

After Charlie Kirk was assassinated at Utah Valley University on September 10, 2025, a crowd of independent researchers started pulling on threads. One of those threads led to Fort Huachuca, and to an alleged meeting there in the weeks leading up to the shooting.

I'm not going to list the names of the people accused of being part of that meeting. They've been named elsewhere. What interests me here is *how* researchers claim they were able to place those names at Huachuca in the first place, because the method is stranger than the accusation.

They didn't find a memo. They found Google Trends.

## The trail

Google Trends is a free tool. You type in a search term and it shows you how much interest there is in that term over time, and where the searching is coming from, down to the city level.

What researchers say they found was a set of names, the same people being accused of attending, showing up as searches tied to Sierra Vista and Fort Huachuca on the dates in question. Ana Escobar laid out what she described as a bank of Google Image searches originating from the base on The Stew Peters Show in July 2026, and others have kept digging since.

Which raises the obvious question. Who sits on an Army intelligence base Googling a list of officials, right before they show up?

## The explanation: an AI that checks its homework

Here's where it gets interesting.

In December 2025, the Pentagon (now calling itself the Department of War) [launched GenAI.mil](https://www.googlecloudpresscorner.com/2025-12-09-Chief-Digital-and-Artificial-Intelligence-Office-Selects-Google-Clouds-AI-to-Power-GenAI-mil), a generative AI platform for its civilian and military workforce, powered by Google's Gemini. The pitch was modernization. Get the paperwork off people's desks.

But according to the researcher, Huachuca didn't wait for the official launch. She says a person working in the base's IT system told her they'd been testing GenAI for a year before it was approved, going back to December 2024. If that's true, the system was already running on base during the late summer of 2025.

The problem with AI doing paperwork is that AI hallucinates. Ask it who someone is and it will happily invent a job title.

Google's fix for that is something called grounding. Instead of answering from memory, the model is forced to run a live Google search and build its answer from what it finds. For a lot of tasks that's a sensible design choice.

Now think about what a base like Huachuca actually does with visitors.

Regular visitors, family members, contractors, delivery drivers, all go through the normal gate systems like DBIDS. Those systems check closed government databases. They're verifying your ID against records the government already holds. They don't go anywhere near the public internet.

Distinguished visitors are different. When someone high-ranking comes through, say a senior Pentagon official or a defense tech CEO, the base has to host them properly. That means a protocol brief, essentially a "who's who" dossier with a bio, a photo, and a current title. If you've ever seen one of these, it looks something like the standard military biography template: rank, name, education, assignments, awards, and a box that says *CURRENT PHOTO IS MANDATORY.*

Current is the key word. People get promoted, change jobs, leave government. So the theory is that this is exactly the kind of task that got automated. A grounded AI pulls each expected VIP's current title and photo from the web, and builds the brief for the day.

According to the researchers' explanation, the lookups ran automatically, just after midnight, on the morning of a visit. The AI would run Google image searches on each name on the daily distinguished visitor log.

And those searches, the theory goes, are what showed up in Google Trends.

## Expected, not necessarily present

If that's right, it means something kind of remarkable. The military's own efficiency upgrade quietly published a guest list.

Not a leak in the usual sense. Nobody decided to release anything. The system just did what it was built to do, and every lookup left a fingerprint in a public tool anyone can access.

It also meant researchers could flip the method around. Instead of starting with names they suspected and checking for searches, they could look at what was being searched from Huachuca and find names *nobody had been talking about*. A visitor list, of sorts, for people they didn't know were expected.

That cuts both ways, though, and it's worth being precise about it. A name showing up in that trail means someone was expected. It doesn't mean they showed up, and it definitely doesn't tell you what they were there for. The searches show a guest list. They don't show the room.

## Where it doesn't quite add up

I like this theory. It's elegant, and it's the kind of thing that actually happens when institutions automate faster than they think through the consequences.

But a few things bother me.

**The timeline.** GenAI.mil officially launched in December 2025. The searches people are pointing to are from late August and early September 2025. The insider's account is what bridges that gap: a year of testing at Huachuca starting in December 2024 would put the system on base right when the searches happened. That's plausible, Fort Huachuca is exactly where the Army tests new IT, and the military was running plenty of AI experiments in 2024. But right now that whole bridge rests on one unnamed person in the base's IT world, relayed secondhand. I haven't seen a document confirming a Gemini-based visitor system running at Huachuca before launch. If one turns up, this part of the theory gets a lot stronger.

**The location.** This is the one I keep coming back to. With grounding, the search isn't run from a computer on base. It's run by Google's own servers on the model's behalf. So why would those searches show up as coming from Sierra Vista at all? If anything, you'd expect automated cloud searches to be filtered out or attributed somewhere else entirely. Human beings on or near the base fit the location data better than an AI does.

**The scale.** Google Trends doesn't show raw search counts. It shows relative interest, scaled from 0 to 100 within each place. In a small town like Sierra Vista, a few searches for an obscure name can spike all the way to 100. A protocol assistant prepping a brief by hand could produce the same pattern.

**The midnight timing.** If somebody really captured searches clustering right after midnight, that would be strong evidence of automation, because people don't usually Google a list of officials at 12:01 a.m. But public Trends data doesn't normally go that granular for old dates. I'd want to know who captured it, and when.

## So who was searching?

Here's what I keep landing on.

If the AI explanation is right, then the Pentagon's rush to modernize accidentally created a public record of who was expected at one of its most sensitive bases, in the exact window people are asking questions about. That's a story about institutions, incentives, and nobody thinking through what "live Google search" means for an intelligence installation.

If the AI explanation is wrong, then the searches are still there. And we're back to the original question, just without the innocent answer.

Somebody at or near Fort Huachuca was looking these people up. Either a machine or a person.

I'd really like to know which.