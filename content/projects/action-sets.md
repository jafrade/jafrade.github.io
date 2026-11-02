---
# Field prefixes say where each field appears:
#   (no prefix) = both the home page card and the case study page
#   card_       = home page project card only
#   page_       = case study page only
#   filter_     = not displayed; used for filtering

title: "Building reusable action sets for HubSpot workflows"
slug: action-sets
order: 5
featured: false
focus: ["Complex workflows", "Systems thinking", "Craft"]

card_thumbnail: images/action-sets/card.jpg
card_context: "HubSpot · B2B CRM · 2023"
card_summary: "Led design and research for HubSpot's Action Sets. About 2,400 customers used them, and 25% of those inserted a set more than 200 times."

page_subtitle: "Saved groups of actions that anyone on a team can drop into a workflow, so builders start from steps their team already worked out."
page_problem: "Teams building lots of workflows rebuilt the same groups of actions in each one, which was slow and made consistency hard to keep."
page_hero_fallback: images/action-sets/hero.jpg
page_metrics:
  - value: "2,400"
    label: "customers used Action Sets within two months of launch"
  - value: "25%"
    label: "of those customers inserted a set more than 200 times, saving each of them at least 3 hours of building"
  - value: "106"
    label: "accounts upgraded to Operations Hub Enterprise, with Action Sets as one of the features behind the upgrade"
page_role_summary: "Lead product designer · Led research and design"
page_timeline: "Apr 2023 – early 2024 (alpha November 2023, launched December 2023, v2 paused early 2024)"
page_shipped_to: "HubSpot Operations Hub Enterprise"
page_chapters:
  - { id: context,  label: "Context",            headline: "Growing teams were building more workflows, with more people building them" }
  - { id: problem,  label: "Problem",            headline: "Customers rebuilt the same steps in every workflow and fixed each copy manually" }
  - { id: strategy, label: "Strategy",           headline: "Discovery calls pointed us to one goal: save a group of actions once and reuse it anywhere" }
  - { id: research, label: "Concept validation", headline: "A comic strip test showed customers expected one edit to reach every copy" }
  - { id: decision, label: "Design direction",   headline: "We shipped independent copies first and designed linked updates for the next release" }
  - { id: solution, label: "Final design",       headline: "Saving and reusing a set works like adding any other action" }
  - { id: impact,   label: "Impact",             headline: "A quarter of the customers using Action Sets inserted a set more than 200 times" }

filter_skills: ["Research", "Interaction design", "Prototyping", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption

  OPEN ITEMS (resolve before packaging)
  1. Metrics: 2,400 customers, 25% inserting more than 200 times, 1 to 2 minutes per insert, and 106 upgrades come from the performance review dated 1/15/2023, which Jason confirmed should read Jan 2024, so the numbers are from within two months of the December 2023 launch. Per-insert time came from a dashboard Jason no longer has (his call to keep). 106 says "contributed", not "caused".
  2. Launch month: alpha Nov 6, 2023 is from the PRD meeting notes; "launched in December" is from the S2 fact bank.
  3. Reorg month isn't in the docs; Jason recalls Feb or Mar 2024, so the page says "early 2024".
  4. Dropped: 128 upgrades in two months (no primary source), the LinkedIn ranking (same), the 87% connected apps (action panel redesign, a different project), the unmoderated UserZoom comic strip results (no notes), and onboarding frames (guided tour and welcome carousel didn't ship).
  5. Concept validation pull quote is from Travis's session notes (a HubSpot partner), in quotation marks there; attribution reads "Customer". Jason chose to swap "Concept A/B" in the quote for the concept names without brackets. Two of the five moderated participants were HubSpot employees; the text says "five people, three of them customers".
  6. Final design frames (create 1-6, add 1-3) need the red annotation callouts removed and "Emma's action set" / "Evan's action set" renamed in Add action set 1. Jason to re-export from Figma, or Claude cleans them.
  7. Final design text: the annotations say the preview moved to a later version and sets are grouped in one accordion. Confirm whether the preview and record-type grouping shipped in v1; text and hero change if not.
  8. Undecided: keep or drop the v1 editing notice image (v1-editing.jpg) in Design direction; keep or drop strategy-1.jpg (early questions list).
  9. Timeline: v1 launched Dec 2023 (Jason). v2 designed and tested Dec 2023 (Jason). v3 iterations Feb 2024 by another designer after the reorg; not shown on the page.
  10. Voice pass.
  11. Focus tags use the new list (Complex workflows, Systems thinking, Craft, AI, Growth, Onboarding, Admin, Reporting, Marketing); skill tag list needs updating. Craft needs specific craft details on the page to back it.
-->

## My role {#role}

I led design and research for Action Sets on the workflows team. I worked with a product manager, a content designer, and four front-end and back-end engineers.

I planned and ran all of the research, from discovery calls and a comic strip concept test to usability testing. I owned the interaction design and specs for the first version, and I designed and tested a second version that linked every copy of a set to the original.

I started on the project in April 2023. The first version went to alpha in November 2023 and launched to Operations Hub Enterprise customers in December 2023. I designed the second version and tested it in December 2023. After a team reorg in early 2024, another designer took over the next round of changes, and the second version never launched.

## 01 · Context {#context}
### Growing teams were building more workflows, with more people building them

HubSpot workflows automate the work behind sales, marketing and operations. Each one starts with a trigger and runs a series of actions, like sending an email, waiting a few days, branching on a property, or running custom code. As customers grow with HubSpot, they build more workflows, and more people on the team start building them.

Action Sets was built for Operations Hub Enterprise, the top plan of HubSpot's product for operations teams. Those customers tend to have larger teams and more complex automation. The people we talked to ranged from one person who owned every workflow to partners building workflows for their clients, and one systems director managed 195 workflows. At that size, the person who owns automation, usually an admin or ops manager, wants the rest of the team to build workflows without things going wrong.

## 02 · Problem {#problem}
### Customers rebuilt the same steps in every workflow and fixed each copy manually

Many workflows share the same pieces: a branch that routes contacts by language, a set of checks before a deal moves forward, or a block of custom code. HubSpot had no way to save those pieces and reuse them. Customers either rebuilt them action by action, or cloned a whole workflow and deleted what they didn't need, which risked missing something in a large one. When a shared piece needed to change, they had to find every workflow that used it and update each one manually.

The requests came from customer feedback surveys, the ideas forum, and support. As more people created workflows, admins saw more inconsistencies and more chances for a workflow to be wrong.

> "Sometimes we make updates which require us to add 15+ actions to several workflows and currently we have to make all of those updates one action at a time."
>
> Customer, HubSpot ideas forum

![The same language branch, rebuilt action by action in every workflow that needed it](images/action-sets/problem-1.jpg)

## 03 · Strategy {#strategy}
### Discovery calls pointed us to one goal: save a group of actions once and reuse it anywhere

The goal was to make building many workflows faster, and to give admins a way to guide their teams. It also gave HubSpot an Enterprise feature that showed workflows could grow with a company.

I planned and ran discovery calls with six customers who cloned workflows often or had asked for this in the ideas forum. Their reuse cases included language branches, deal checks, custom code, and the same email campaign across several blogs. They wanted it to save time, keep their work accurate, and keep workflows consistent. Most reuses weren't exact copies, since a property or an email often changed each time. Everyone we asked wanted to control who could edit a shared set, though no one said it would stop them from using it. A few already reused work in other tools, like Zapier's Sub-Zaps, and liked that a change made in one place reached everywhere it was used.

> "I want a head start. I don't want to always have to start from scratch."
>
> Customer, discovery call

From there my PM and I scoped the idea: let customers save a group of actions as a kind of mini template, find it in the action panel, and add it to any workflow of the same type.

![The early questions my content designer and I worked through: what a reusable set is, who it's for, and how editing copies should work](images/action-sets/strategy-1.jpg)

## 04 · Concept validation {#research}
### A comic strip test showed customers expected one edit to reach every copy

We had two very different ways to build this and needed customer reactions before designing either in detail. A prototype would have pulled people into the UI, so I used a comic strip test. Each concept was a short story of two coworkers, where one saves a language branch and the other reuses it.

In the Saved Actions concept, the actions were a new kind of action you drag onto the canvas, and you could change your copy freely. In the Shared Workflow concept, the actions were their own workflow, and other workflows sent contacts to it and waited for them to come back.

<!-- carousel -->
![Saved Actions: Jason needs to build a new workflow](images/action-sets/concept-a-1.jpg)
![He and Emma keep rebuilding the same language branch, so he decides to save it](images/action-sets/concept-a-2.jpg)
![He selects the branch and its actions, and names it so Emma will recognize it](images/action-sets/concept-a-3.jpg)
![Emma finds the saved branch in her actions and drags it onto her workflow](images/action-sets/concept-a-4.jpg)
![She deletes the part she doesn't need](images/action-sets/concept-a-5.jpg)
![She publishes her workflow with the saved branch, changed to fit her needs](images/action-sets/concept-a-6.jpg)
<!-- /carousel -->

<!-- carousel -->
![Shared Workflow: Jason needs to build a new workflow](images/action-sets/concept-b-1.jpg)
![He decides to clone the language branch and rename it so the team can reuse it](images/action-sets/concept-b-2.jpg)
![He removes the other actions and sets it to run only when contacts are sent from other workflows](images/action-sets/concept-b-3.jpg)
![When contacts finish the branch, they return to the workflow they came from](images/action-sets/concept-b-4.jpg)
![Emma sends her contacts to Jason's branch instead of building it herself](images/action-sets/concept-b-5.jpg)
![The branch has steps she doesn't need, so she clones it rather than break Jason's version](images/action-sets/concept-b-6.jpg)
![She removes the extra actions, renames her copy, and publishes it](images/action-sets/concept-b-7.jpg)
![Back in her workflow, she sends contacts to her own copy](images/action-sets/concept-b-8.jpg)
<!-- /carousel -->

I ran it with five people, three of them customers. Three picked Saved Actions outright, and the other two wanted parts of both.

> "The 'Shared Workflow' concept seems like a beta version of the 'Saved Actions' concept."
>
> Customer, comic strip test

The biggest finding was about editing. Most people assumed a change to the saved set would update every workflow that used it, and that editing a copy in your own workflow would break it away from the original. They didn't want changes pushed out without warning, and one person asked for a draft step so edits could be reviewed before they went live. I went with Saved Actions, since most people preferred it, and linked updates became the core of the second version.

## 05 · Design direction {#decision}
### We shipped independent copies first and designed linked updates for the next release

After the comic strip test, I worked out where sets would live and how people would build them, starting with low-fidelity wireframes of saved "snippets" in the action panel. We considered three ways to build a set: as a single collapsed action, as a container around actions on the canvas, and in its own editor. We went with the editor, since building on the canvas wasn't technically feasible at the time.

<!-- carousel -->
![A set shown as a single collapsed action](images/action-sets/build-1.jpg)
![A set built as a container around actions on the canvas](images/action-sets/build-2.jpg)
![A set built in its own editor, the direction we shipped](images/action-sets/build-3.jpg)
<!-- /carousel -->

Participants didn't agree on a name. They called it a saved branch, a mini flow, a block, and a template. Our content designer made the case for the strongest options, and the team chose "action sets." It did slightly better in the moderated test, held up in unmoderated testing, and avoided "template," which already meant something else in workflows.

![The naming matrix we used to compare templates, blocks, modules and sets](images/action-sets/naming.jpg)

Our original design linked every copy to the original set, which is what customers expected. Engineering pushed back on what was feasible for the first release. Rather than delay it, my PM and I agreed to ship sets as independent copies, since saving and reusing actions was valuable on its own. My job was to make the difference clear to customers. The panel says that changes to your copy won't affect the original set, and editing the original shows a notice that workflows already using it won't change.

![Editing the original set, with a notice that existing workflows keep their copy](images/action-sets/v1-editing.jpg)

While v1 was being built, I designed v2: global action sets. I mapped how creating, updating and detaching would work, and how publishing should behave when a change could break workflows that already used the set.

![The v2 concepts: the original set and its copies, and what happens when you publish a change](images/action-sets/v2-concepts.jpg)

I also explored how a global set should show up on the canvas. Collapsing it into a single action would have hidden what the set was doing, and it raised questions about branches and execution logs. So we tested a version that kept every action visible and tagged each one with the set it came from.

![Explorations for showing a global set on the canvas, with my notes on the tradeoffs](images/action-sets/v2-canvas-explorations.jpg)

<!-- carousel -->
![The prototype we tested: turning on Global when creating a set](images/action-sets/v2-test-1.jpg)
![The set's settings: Global, allow detaching, editing permissions, and the workflows that use it](images/action-sets/v2-test-2.jpg)
![Detaching a set's actions inside a workflow](images/action-sets/v2-test-3.jpg)
![A workflow showing that its set has an update to review](images/action-sets/v2-test-4.jpg)
<!-- /carousel -->

In December 2023, I tested the prototype with six workflow builders in an unmoderated study. Only two of the six found the global setting when creating a set, and average confidence was 3 out of 7. All five who updated a set expected the change to reach other workflows automatically, not after a manual update. When we asked what "global action set" meant, the answers were all over the place.

> "I believe it means that it will send [an] outreach in a different language."
>
> Participant, v2 usability test

## 06 · Final design {#solution}
### Saving and reusing a set works like adding any other action

<!-- carousel -->
![A set in a workflow, with its description and preview in the side panel](images/action-sets/final-1.jpg)
![Creating a set from the action panel, from scratch or from the current workflow](images/action-sets/final-2.jpg)
![Building the set in its own editor](images/action-sets/final-3.jpg)
![Sets listed in the action panel, with a tip explaining why one might be missing](images/action-sets/final-4.jpg)
<!-- /carousel -->

Once we agreed to ship sets as independent copies, we finished the first version around our original goal: making it faster to build workflows that share the same steps.

We put action sets in the action panel next to HubSpot's own actions, so adding a set works the same way as adding any other action. That kept it familiar, since the Shared Workflow concept had confused some people in testing.

Customers can save a group of actions as a set, starting from scratch or from the workflow they're in, and build it in its own editor. Sets are grouped by the type of record they work with, and a tip explains why one might be missing. Each set shows a description and a preview before you add it, and it can go anywhere in a workflow, including inside a branch. Once it's in, its actions can be changed like any others.

Action Sets went to alpha in November 2023 and launched to Operations Hub Enterprise customers in December 2023.

## 07 · Impact {#impact}
### A quarter of the customers using Action Sets inserted a set more than 200 times

Customers had been rebuilding the same steps in workflow after workflow. Within two months of launch, about 2,400 customers used Action Sets.

- 25% of the 2,400 customers inserted a set more than 200 times.
- Each insert saved about 1 to 2 minutes of building the same actions again.
- For those heavy users, that added up to at least 3 hours each.

Action Sets was part of Operations Hub Enterprise, and it contributed to 106 accounts upgrading to that plan.

The linked updates customers asked for in research never shipped. After a team reorg in early 2024, another designer iterated on the version I tested, but it was deprioritized before launch.

## Reflection {#reflection}
### What I'd do differently

Looking back, I would have spent more time weighing what people preferred against what it would take to build and how easy it would be to use. Saved Actions was the concept people preferred, but it was much more technically complicated to build.

The comic strip test was good for early reactions without influencing too much, but it made it hard to judge how something works when you can't click through it. If I'd pushed for testing with a working prototype, we might have learned that the Shared Workflow concept would have been just as successful and a lot easier to build.

I'd also keep the scope tighter. I folded saving custom code into Action Sets, hoping to solve both problems at once. But people think of their code as a single file they reuse, not a group of actions, and that should have been its own feature.
