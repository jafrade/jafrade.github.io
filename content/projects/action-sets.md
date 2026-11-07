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
card_context: "HubSpot · Workflow automation · 2023"
card_summary: "Led design and research for HubSpot's Action Sets. They contributed to 106 upgrades to Operations Hub Enterprise, and about 2,400 customers used them within two months."

page_overview: "Ops teams were rebuilding the same steps in workflow after workflow, which was slow and led to more mistakes as more people built them. HubSpot also needed Enterprise features that made upgrading worth it. We built Action Sets, saved groups of actions anyone on the team can reuse in any workflow."
page_hero_fallback: images/action-sets/hero.jpg
page_metrics:
  - value: "106"
    label: "accounts upgraded to Operations Hub Enterprise, with Action Sets as one of the features behind the upgrade"
  - value: "2,400"
    label: "customers used Action Sets within two months of launch"
  - value: "25%"
    label: "of those customers inserted a set more than 200 times, saving each of them at least 3 hours of rebuilding the same steps"
page_role_summary: "Lead product designer · Led research and design"
page_timeline: "Apr 2023 – early 2024 (alpha November 2023, launched December 2023, v2 paused early 2024)"
page_shipped_to: "HubSpot Operations Hub Enterprise"
page_chapters:
  - { id: context,  label: "Context",            headline: "Enterprise teams had a lot of people building a lot of workflows" }
  - { id: problem,  label: "Problem",            headline: "Customers rebuilt the same steps in every workflow, then fixed each copy by hand" }
  - { id: strategy, label: "Strategy",           headline: "Six discovery calls turned a pile of requests into one idea" }
  - { id: research, label: "Concept validation", headline: "We drew a comic strip, and customers told us edits should reach every copy" }
  - { id: decision, label: "Key decisions",      headline: "Engineering said linked updates had to wait, so we shipped copies first" }
  - { id: solution, label: "Final design",       headline: "Adding a set works just like adding any other action" }
  - { id: impact,   label: "Impact",             headline: "Action Sets contributed to 106 Enterprise upgrades" }

filter_skills: ["Research", "Interaction design", "Prototyping", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption
  - Top of page layout: context line, title, page_overview (in the spot the old subtitle used), focus tags, hero, then a full-width Results row with the three page_metrics side by side (number above label), then My role, Timeline and Shipped to below. page_subtitle and page_problem are retired; remove the subtitle and the "The problem" block.
  - Key decisions (05) uses "####" subheads to separate its four decisions. Style them smaller than the chapter headline.

  SOURCES AND KNOWN ITEMS (for reference, nothing here renders)
  - Metrics (2,400 customers, 25% inserting a set more than 200 times, 1 to 2 minutes per insert, 106 upgrades) come from Jason's performance review dated Jan 2024, within two months of the December 2023 launch. The per-insert time came from a dashboard Jason no longer has. 106 says "contributed", not "caused".
  - Alpha Nov 6, 2023 is from the PRD meeting notes. The reorg month isn't in the docs, so the page says "early 2024".
  - v1 launched Dec 2023 (Jason). v2 designed and tested Dec 2023 (Jason). v3 iterations in Feb 2024 were by another designer after the reorg and aren't shown.
  - The Concept validation pull quote is from Travis's session (a HubSpot partner). Jason chose to swap "Concept A/B" for the concept names without brackets.
  - The hero frame's panel copy describes linked updates (v2 behavior); v1 shipped unlinked copies.
-->

## My role {#role}

I led design and research for Action Sets on the workflows team. I worked with a product manager, a content designer, and four front-end and back-end engineers.

I planned and ran all of the research, from discovery calls and a comic strip concept test to usability testing. I owned the interaction design and specs for the first version, and I designed and tested a second version that linked every copy of a set to the original.

I started on the project in April 2023. The first version went to alpha in November 2023 and launched to Operations Hub Enterprise customers in December 2023. I designed the second version and tested it in December 2023. After a team reorg in early 2024, another designer took over the next round of changes, and the second version never launched.

## 01 · Context {#context}
### Enterprise teams had a lot of people building a lot of workflows

HubSpot workflows automate the work behind sales, marketing and operations. Each one starts with a trigger and runs a series of actions, like sending an email, waiting a few days, branching on a property, or running custom code. As customers grow with HubSpot, they build more workflows, and more people on the team start building them.

On Operations Hub Enterprise, HubSpot's top plan for operations teams, that adds up fast. One systems director we talked to managed nearly 200 workflows. The person who owns automation, usually an admin or ops manager, wants the rest of the team to build workflows without things going wrong.

## 02 · Problem {#problem}
### Customers rebuilt the same steps in every workflow, then fixed each copy by hand

Many workflows share the same pieces: a branch that routes contacts by language, a set of checks before a deal moves forward, or a block of custom code. HubSpot had no way to save those pieces and reuse them. Customers either rebuilt them action by action, or cloned a whole workflow and deleted what they didn't need, which risked missing something in a large one. When a shared piece needed to change, they had to find every workflow that used it and update each one manually.

As more people created workflows, admins saw more inconsistencies and more chances for a workflow to be wrong. One customer wrote on the ideas forum, "Sometimes we make updates which require us to add 15+ actions to several workflows and currently we have to make all of those updates one action at a time."

> "Sometimes we make updates which require us to add 15+ actions to several workflows and currently we have to make all of those updates one action at a time."
>
> Customer, HubSpot ideas forum

![The same language branch, rebuilt action by action in every workflow that needed it](images/action-sets/problem-1.jpg)

The problem was worst for large teams with several people building workflows, which made it a good fit for Enterprise, where HubSpot wanted more advanced features that gave customers a reason to upgrade.

Customer feedback told us what people wanted. What we didn't know yet was how they actually reused their work. That gave us our question: how might we make building many workflows faster and safer for large teams, in a way that makes Enterprise worth upgrading to?

## 03 · Strategy {#strategy}
### Six discovery calls turned a pile of requests into one idea

The goal was to make building many workflows faster, and to give admins a way to guide their teams.

I planned and ran discovery calls with six customers who cloned workflows often or had asked for this in the ideas forum. Their reuse cases included language branches, deal checks, custom code, and the same email campaign across several blogs. They wanted it to save time, keep their work accurate, and keep workflows consistent. As one put it, "I want a head start. I don't want to always have to start from scratch." Most reuses weren't exact copies, since a property or an email often changed each time. Everyone we asked wanted to control who could edit a shared set, though no one said it would stop them from using it. A few already reused work in other tools, like Zapier's Sub-Zaps, and liked that a change made in one place reached everywhere it was used.

> "I want a head start. I don't want to always have to start from scratch."
>
> Customer, discovery call

From there my PM and I scoped the idea: let customers save a group of actions as a kind of mini template, find it in the action panel, and add it to any workflow of the same type.

## 04 · Concept validation {#research}
### We drew a comic strip, and customers told us edits should reach every copy

We had two very different ways to build this and needed customer reactions before designing either in detail. A prototype would have pulled people into the UI, so I used a comic strip test. Each concept was a short story of two coworkers, where one saves a language branch and the other reuses it.

In the Saved Actions concept, the actions were a new kind of action you drag onto the canvas, and you could change your copy freely. In the Shared Workflow concept, the actions were their own workflow, and other workflows sent contacts to it and waited for them to come back.

<!-- carousel -->
![Saved Actions: the whole story on one page](images/action-sets/concept-a-summary.jpg)
![Jason needs to build a new workflow](images/action-sets/concept-a-1.jpg)
![He and Emma keep rebuilding the same language branch, so he decides to save it](images/action-sets/concept-a-2.jpg)
![He selects the branch and its actions, and names it so Emma will recognize it](images/action-sets/concept-a-3.jpg)
![Emma finds the saved branch in her actions and drags it onto her workflow](images/action-sets/concept-a-4.jpg)
![She deletes the part she doesn't need](images/action-sets/concept-a-5.jpg)
![She publishes her workflow with the saved branch, changed to fit her needs](images/action-sets/concept-a-6.jpg)
<!-- /carousel -->

<!-- carousel -->
![Shared Workflow: the whole story on one page](images/action-sets/concept-b-summary.jpg)
![Jason needs to build a new workflow](images/action-sets/concept-b-1.jpg)
![He decides to clone the language branch and rename it so the team can reuse it](images/action-sets/concept-b-2.jpg)
![He removes the other actions and sets it to run only when contacts are sent from other workflows](images/action-sets/concept-b-3.jpg)
![When contacts finish the branch, they return to the workflow they came from](images/action-sets/concept-b-4.jpg)
![Emma sends her contacts to Jason's branch instead of building it herself](images/action-sets/concept-b-5.jpg)
![The branch has steps she doesn't need, so she clones it rather than break Jason's version](images/action-sets/concept-b-6.jpg)
![She removes the extra actions, renames her copy, and publishes it](images/action-sets/concept-b-7.jpg)
![Back in her workflow, she sends contacts to her own copy](images/action-sets/concept-b-8.jpg)
<!-- /carousel -->

I ran it with five people, three of them customers. Three picked Saved Actions outright, and the other two wanted parts of both. One said, "The 'Shared Workflow' concept seems like a beta version of the 'Saved Actions' concept."

> "The 'Shared Workflow' concept seems like a beta version of the 'Saved Actions' concept."
>
> Customer, comic strip test

The biggest finding was about editing. Most people assumed a change to the saved set would update every workflow that used it, and that editing a copy in your own workflow would break it away from the original. They didn't want changes pushed out without warning, and one person asked for a draft step so edits could be reviewed before they went live. I went with Saved Actions, since most people preferred it, and linked updates became the core of the second version.

## 05 · Key decisions {#decision}
### Engineering said linked updates had to wait, so we shipped copies first

#### Where sets get built

After the comic strip test, I worked out where sets would live and how people would build them, starting with low-fidelity wireframes of saved "snippets" in the action panel. We considered three ways to build a set: as a single collapsed action, as a container around actions on the canvas, and in its own editor. We went with the editor, since building on the canvas wasn't technically feasible at the time.

<!-- carousel -->
![Early wireframes of saved "snippets": finding, previewing, selecting and saving groups of actions](images/action-sets/build-0a.jpg)
![The three build types side by side: a collapsed action, a container on the canvas, and a separate editor](images/action-sets/build-0b.jpg)
![A set shown as a single collapsed action](images/action-sets/build-1.jpg)
![A set built as a container around actions on the canvas](images/action-sets/build-2.jpg)
![A set built in its own editor, the direction we shipped](images/action-sets/build-3.jpg)
<!-- /carousel -->

#### What to call them

Participants didn't agree on a name. They called it a saved branch, a mini flow, a block, and a template. Our content designer made the case for the strongest options, and the team chose "action sets." It did slightly better in the moderated test, held up in unmoderated testing, and avoided "template," which already meant something else in workflows.

![The naming matrix we used to compare templates, blocks, modules and sets](images/action-sets/naming.jpg)

#### Shipping copies before linked updates

Our original design linked every copy to the original set, which is what customers expected. Engineering pushed back on what was feasible for the first release. Rather than delay it, my PM and I agreed to ship sets as independent copies, since saving and reusing actions was valuable on its own. My job was to make the difference clear to customers. The panel says that changes to your copy won't affect the original set, and editing the original shows a notice that workflows already using it won't change.

#### Designing linked updates for v2

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

In December 2023, I tested the prototype with six workflow builders in an unmoderated study. Only two of the six found the global setting when creating a set, and average confidence was 3 out of 7. All five who updated a set expected the change to reach other workflows automatically, not after a manual update. When we asked what "global action set" meant, the answers were all over the place. One participant said, "I believe it means that it will send [an] outreach in a different language."

> "I believe it means that it will send [an] outreach in a different language."
>
> Participant, v2 usability test

## 06 · Final design {#solution}
### Adding a set works just like adding any other action

<!-- carousel -->
![A set's description and preview before adding it to a workflow](images/action-sets/final-1.jpg)
![The action panel before any sets exist, with Create action set next to HubSpot's actions](images/action-sets/final-2.jpg)
![Creating a set: name it, then copy the actions from the current workflow or start from scratch](images/action-sets/final-3.jpg)
![Building the set in its own editor](images/action-sets/final-4.jpg)
![Editing the set's name and description](images/action-sets/final-5.jpg)
![A confirmation that says where to find the new set](images/action-sets/final-6.jpg)
![Saved sets listed in the action panel](images/action-sets/final-7.jpg)
![The set's actions added to a workflow, inside a branch, where they can be changed like any others](images/action-sets/final-8.jpg)
<!-- /carousel -->

Once we agreed to ship sets as independent copies, we finished the first version around our original goal: making it faster to build workflows that share the same steps.

We put action sets in the action panel next to HubSpot's own actions, so adding a set works the same way as adding any other action. That kept it familiar, since the Shared Workflow concept had confused some people in testing.

Customers can save a group of actions as a set, starting from scratch or from the workflow they're in, and build it in its own editor. Saved sets appear in their own section of the action panel. Each set shows a description and a preview before you add it, and it can go anywhere in a workflow, including inside a branch. Once it's in, its actions can be changed like any others.

Action Sets went to alpha in November 2023 and launched to Operations Hub Enterprise customers in December 2023.

## 07 · Impact {#impact}
### Action Sets contributed to 106 Enterprise upgrades

**Action Sets was one of the features behind 106 accounts upgrading to Operations Hub Enterprise.**

Within two months of launch, **about 2,400 customers had used Action Sets**, and **a quarter of them inserted a set more than 200 times. That saved each of those heavy users at least 3 hours of rebuilding the same steps.**

The linked updates customers asked for in research never shipped. After a team reorg in early 2024, another designer iterated on the version I tested, but it was deprioritized before launch.

## Reflection {#reflection}
### What I'd do differently

Looking back, I would have spent more time weighing what people preferred against what it would take to build and how easy it would be to use. Saved Actions was the concept people preferred, but it was much more technically complicated to build.

The comic strip test was good for early reactions without influencing too much, but it made it hard to judge how something works when you can't click through it. If I'd pushed for testing with a working prototype, we might have learned that the Shared Workflow concept would have been just as successful and a lot easier to build.

I'd also keep the scope tighter. I folded saving custom code into Action Sets, hoping to solve both problems at once. But people think of their code as a single file they reuse, not a group of actions, and that should have been its own feature.
