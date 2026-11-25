---
# DRAFT: decision-first redraft of content/projects/embedded-automate-panel.md.
# Build with: python3 tools/build.py --draft content/drafts/embedded-automate-panel.md
# Writes work/embedded-automate-panel-draft.html (unlisted, noindex). The live page is unchanged.

title: "Redesigning HubSpot's embedded automation"
slug: embedded-automate-panel
order: 1
featured: true
focus: ["Craft", "AI", "Complex workflows", "Systems thinking"]

card_thumbnail: images/embedded-automate-panel/hero.jpg
card_context: "HubSpot · Workflow automation · 2026"
card_summary: "Led design and co-led strategy for HubSpot's Automate panel. The panel doubled the number of workflows Starter customers created each week, and 72% of them used features new to Starter."

page_overview: "Small business customers were leaving HubSpot because they couldn't find the automation they needed. It was scattered across five patterns, each on its own screen. We built one Automate panel that opens on the pages where they already work, and every automation in it is a real workflow they can grow into."
page_key_decision: "I proposed bringing automation to the pages where customers already work, instead of giving them another place to go for it. Every automation would be a real workflow, so someone could start simple on a deal page and later open the same automation in the full Workflows app after upgrading to Pro. Before another team would give us a button on their page, we had to prove it with an A/B test. Discovery tripled."
page_hero_fallback: images/embedded-automate-panel/hero.jpg
page_metrics:
  - value: "2×"
    label: "as many workflows created each week by Starter customers in the month after launch"
  - value: "45%"
    label: "of AI-recommended workflows went live, twice the rate of starting from a blank page"
  - value: "72%"
    label: "of panel workflows used automation Starter customers never had before"
page_role_summary: "Lead product designer · Co-led vision with PM"
page_timeline: "Feb – Oct 2026 (beta July 23, launched to all Starter customers July 28–30, iterated through October)"
page_shipped_to: "HubSpot Starter"
page_chapters:
  - { id: context,  label: "Context",            headline: "Starter customers have a business to run and no time to learn automation" }
  - { id: problem,  label: "Problem",            headline: "Starter customers were leaving because finding automation was an Easter egg hunt" }
  - { id: strategy, label: "Strategy",           headline: "I proposed one way to automate, on every page, with a real workflow behind it" }
  - { id: research, label: "Concept validation", headline: "We had to earn a button on another team's page" }
  - { id: decision, label: "Key decisions",      headline: "One builder had to work for first-timers and for customers moving up to Pro" }
  - { id: solution, label: "Final design",       headline: "Automation now reads like a sentence and lives where the work happens" }
  - { id: impact,   label: "Impact",             headline: "Starter customers built twice as many workflows a week" }

filter_skills: ["Strategy", "Research", "AI and LLM design", "Interaction design", "Prototyping", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - New field page_key_decision: shown under the overview in the hero, labeled "Key decision". Not part of the case-study skill yet; add it to the skill's top-of-page rules if this sticks.
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption
  - Key decisions (05) uses "####" subheads to separate its three decisions. Style them smaller than the chapter headline.
  - The how-might-we question is its own paragraph at the end of Problem, starting "That gave us our question:".
-->

## My role {#role}

I led design for the Automate panel and co-led the vision with my PM, starting with the proposal to bring automation onto the pages where customers already work. I worked with six front-end and back-end engineers, and with partner product teams who reviewed the design and placement of the panel on their pages.

I owned the interaction and visual design, from the first concepts in Lovable to the final specs in Figma. I also ran the research, wrote the framework for how AI recommendations explain themselves, and built the rulebook and agent skill that write each automation's sentence.

I started on the project in February 2026. The panel went to beta on July 23 and launched to all Starter customers by July 30, and I kept improving it through October.

## 01 · Context {#context}
### Starter customers have a business to run and no time to learn automation

HubSpot Starter is the entry-level paid plan, used by more than 150,000 customers, mostly founders and early hires at companies with 1 to 25 people. They're wearing a lot of hats, and their attention is on finding customers and growing the business. Learning a tool like HubSpot, and automation in particular, feels like a big investment of time they don't have. What they need is simple: leads that don't fall through the cracks, deals that get followed up on, and tasks that get created without doing it manually.

## 02 · Problem {#problem}
### Starter customers were leaving because finding automation was an Easter egg hunt

HubSpot was losing Starter customers, and fewer new accounts were signing up. When an analyst dug into why customers were leaving, about a third were leaving because they didn't have the automation they needed to run their business. With fewer customers staying and fewer coming in, fewer were upgrading to Pro, and upgrades are a big part of how HubSpot keeps customers and grows revenue.

Much of what they needed was already in Starter, but customers couldn't find it. Starter didn't have a central Workflows app, so their automation was scattered across five different patterns, each with its own UI, entry point and permissions. Some lived in settings, some lived inside individual apps, and some weren't visible anywhere. One customer described finding the automations tied to their records as "a little bit of an Easter egg hunt."

> "A little bit of an Easter egg hunt."
>
> Customer, describing how they found existing automations

<!-- carousel -->
![Our audit of every automation surface in HubSpot, from pipeline settings to rulesets to sequences](images/embedded-automate-panel/problem-1.jpg)
![A few of those patterns as customers saw them: forms, deal pipelines, privacy settings, quotes, and the prospecting agent](images/embedded-automate-panel/problem-2.jpg)
<!-- /carousel -->

Automating a simple task meant leaving your work to find the right screen, figuring out how that screen worked, and then coming back later to check what was running. Adoption stayed low, and Starter customers who couldn't get what they needed were leaving to find other tools.

We measured progress with two numbers: the share of Starter customers who created a workflow, which we aimed to raise from 60% to 70%, and the share who turned one on.

That gave us our question: how might we make automation easy for Starter customers to find and use, so more customers sign up and stay, and upgrading to Pro feels like a natural next step?

## 03 · Strategy {#strategy}
### I proposed one way to automate, on every page, with a real workflow behind it

We'd already tried pointing people to automation. Before this project, my team built a home page for automation that linked customers to all of these tools. It helped them find automation, but they still had to leave their work to use it, and the five patterns behind it were as scattered as ever.

My PM and I started with a brainstorm, and the idea that shaped everything after it was that they're all workflows. Every embedded automation, wherever it showed up, could be backed by a real workflow. Someone could start with something simple on a deal page and later open the same automation in the full Workflows app without rebuilding it, which would also make the move to Pro easier.

From there I proposed a single Automate experience that would look and work the same on every page where people already do their work. AI-generated recommendations, based on how each customer used their account, would show them where to start.

<!-- carousel -->
![The new approach: every embedded automation is a workflow](images/embedded-automate-panel/strategy-4.jpg)
![Core problems and what customers needed](images/embedded-automate-panel/strategy-3.jpg)
![The full brainstorm board, including our vision for the whole system: embedded experience, unified canvas, unified management, and agents](images/embedded-automate-panel/strategy-1.jpg)
<!-- /carousel -->

The bet came with two costs. Our button would have to live on pages other teams owned, and we'd need a builder simple enough for a first-timer that still led somewhere for customers who upgraded. The next two chapters are how we earned each one.

## 04 · Concept validation {#research}
### We had to earn a button on another team's page

The deal records page belonged to another team, who had been simplifying record pages by moving buttons into menus to cut clutter. They worried a new button would add clutter without enough people getting value from it, and saw a rise in clicks as a vanity metric.

So we ran an A/B test that moved the Automate button from settings onto the deal records page. Discovery went up 3x, and activation, meaning customers created a workflow, went up 2x. The result was statistically significant. The activation result showed that people who found the button went on to build automations, and we used it to show the team that owned the page, and their leadership, that the button was worth the space.

We then tested our first node and card concept for the panel with 12 customers, to check whether the new builder was easy to understand and use. Having automation right on the page made sense to them, and pre-filling the trigger from the record they were viewing made the biggest difference. One person said, "It's remembered all the context I've gone through. I haven't got to reselect or hunt for it."

> "It's remembered all the context I've gone through. I haven't got to reselect or hunt for it."
>
> Customer, concept test

<!-- carousel -->
![The Automate button on the deals page](images/embedded-automate-panel/concept-1.jpg)
![Recommended workflows and the deal pipeline automations in one place](images/embedded-automate-panel/concept-2.jpg)
![A template's details before creating it](images/embedded-automate-panel/concept-3.jpg)
![AI builds the workflow from the template](images/embedded-automate-panel/concept-4.jpg)
![The first node and card builder, with the assistant next to it](images/embedded-automate-panel/concept-5.jpg)
<!-- /carousel -->

One finding changed our plans: recommendations felt like ads unless they fit what the person was doing and explained why they mattered. That led to the recommendation framework in the next chapter.

## 05 · Key decisions {#decision}
### One builder had to work for first-timers and for customers moving up to Pro

#### Sentences or nodes

The builder had two audiences pulling in different directions. Partner teams and leadership thought it looked too technical for first-timers, and that writing each automation as a plain sentence ("When a deal moves to Closed Won, create a task for the deal owner") would make it easier. My team wanted to build on the node-and-card pattern from the Workflows app, so customers who upgraded to Pro would already know the full app. Our first brainstorm also listed the costs of sentences: lots of custom UI to build, and they might not translate well.

![Early pros and cons: sentence-style builder vs. AI-first creation](images/embedded-automate-panel/pros-cons.jpg)

![Three builder styles we explored, rules, sentences, and workflow nodes, each in a split or full view](images/embedded-automate-panel/explorations.jpg)

We took that feedback and built two Lovable prototypes to see whether one was actually easier to use. Customers were split. People who liked the sentence version said it felt "less like programming and more like just editing a Word doc." People who liked the node and canvas version said, "Makes me feel like I am building a workflow. Nodes are familiar."

> "Less like programming and more like just editing a Word doc."
>
> Customer who preferred the sentence version

> "Makes me feel like I am building a workflow. Nodes are familiar."
>
> Customer who preferred the node and canvas version

The test also showed something I didn't expect: the builder's design changed how people used AI. In the sentence version, people typed their changes to the AI. In the node and canvas version, they edited the cards directly.

![The sentence version and the node and canvas version, side by side as tested](images/embedded-automate-panel/research-styles.jpg)

With customers split, we went with the sentence version the stakeholders favored, and my job became making it work at scale.

#### Making the sentence version work

I led the visual design from there, starting with how the sentences should look. I tried a few builder layouts, from plain sentences to each step in its own card, and several styles for the parts people could edit, including tinted chips, bold underlined text, and dashed outlines for empty fields.

<!-- carousel -->
![Builder layout: plain sentences with no containers](images/embedded-automate-panel/builder-1.jpg)
![Builder layout: each step in its own card](images/embedded-automate-panel/builder-2.jpg)
![Builder layout: connected cards on a gray background](images/embedded-automate-panel/builder-3.jpg)
![Token styles: tinted chips colored by action type, compared with bold underlined text](images/embedded-automate-panel/tokens-1.jpg)
![Token styles: a single accent color, compared with dashed outlines on empty fields](images/embedded-automate-panel/tokens-2.jpg)
<!-- /carousel -->

My biggest concern had been scale, since every action needs its own sentence. So I built a rulebook and an agent skill that read an action's definition (its field labels, input order, and dependencies) and write its sentence automatically, for every existing and future action. The definition decides the structure, and the skill only handles the grammar. Because every sentence is still a real workflow underneath, customers who upgrade can open it in the full app.

Translation was the tradeoff we accepted. Each sentence follows the order of the fields in the form, so translators can change the words but can't reorder them. In languages with a different word order, some sentences read less naturally.

#### Recommendations that explain themselves

Because recommendations felt like ads in research, I wrote a framework for how they explain themselves. Each one says what it will do for the business, never why HubSpot picked it. Accounts with enough activity see real evidence, like "28x this week deal owners were manually assigned," and newer accounts get suggestions that teach good habits instead.

## 06 · Final design {#solution}
### Automation now reads like a sentence and lives where the work happens

<!-- carousel -->
![The Automate button on the contacts page](images/embedded-automate-panel/final-01.jpg)
![The panel opens with suggestions. A newer account sees automations that teams commonly set up first](images/embedded-automate-panel/final-02.jpg)
![Picking a suggestion opens it as a sentence, with the trigger filled in and the assistant beside it](images/embedded-automate-panel/final-03.jpg)
![Selecting an empty field to edit it in place](images/embedded-automate-panel/final-04.jpg)
![Typing a task title, then adding data from the trigger](images/embedded-automate-panel/final-05.jpg)
![Picking the contact's first name from the trigger data](images/embedded-automate-panel/final-06.jpg)
![The task title now includes the contact's first name](images/embedded-automate-panel/final-07.jpg)
![Adding another step from the action menu](images/embedded-automate-panel/final-08.jpg)
![A delay added as the next step, ready to publish](images/embedded-automate-panel/final-09.jpg)
<!-- /carousel -->

We finalized the visual and interaction design around the question we started with: making automation easy to find and use.

We created a globally recognizable button that could be added to any app, and it passes that app's context into the Automate panel. Customers can start from suggestions based on that context and their team's activity, or create an automation from scratch or from a template. Picking one fills in the trigger based on where they opened the panel. Each automation reads as a sentence with the editable parts highlighted, so they can change a field in place, pull in data from the trigger, or ask the assistant beside it to make the change. Automations already set up for that page are listed below the suggestions.

The panel went to beta on July 23, 2026, and reached every Starter account by July 30.

## 07 · Impact {#impact}
### Starter customers built twice as many workflows a week

Through the end of August, Starter customers created twice as many workflows each week as they did before the panel launched, and 72% of the workflows built in the panel used features Starter didn't have before. About a third of the workflows started in the panel went live. The ones that started from an AI recommendation went live 45% of the time, about twice the rate of workflows built from scratch.

The panel was part of a bigger push on Starter that started with the Starter version of the Automation Overview in January. From January to August, the share of Starter customers who created a workflow rose from 60% to 75%, beating our 70% goal, and the share who turned one on rose from 40% to 60%.

We tracked upgrades to Pro as well, but I don't have final results to share.

Because every automation was a real workflow, the panel could be reused, and Agent Hub Starter did. It launched on September 21 with the panel as its builder, and gave Starter customers one place to create and manage all their workflows for the first time. The number of workflows turned on each week more than tripled in the weeks after.

## Reflection {#reflection}
### What I'd do differently

The A/B test on the deal page worked because it gave everyone the same evidence. I'd bring that to the builder debate sooner. Our brainstorm weighed build time, scalability and translation, but we didn't lay those tradeoffs out clearly for stakeholders, so the conversation stayed on which version looked easier.

I'd also test more ideas, and test them sooner. Putting several directions in front of customers early would have given everyone the same evidence to work from.

Once we committed to the sentence version, my job was to make it work. The scaling problem I'd worried about is what led me to build the rulebook and skill.
