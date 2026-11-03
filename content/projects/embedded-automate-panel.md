---
# Field prefixes say where each field appears:
#   (no prefix) = both the home page card and the case study page
#   card_       = home page project card only
#   page_       = case study page only
#   filter_     = not displayed; used for filtering

title: "Redesigning HubSpot's embedded automation"
slug: embedded-automate-panel
order: 1
featured: true
focus: ["Craft", "AI", "Complex workflows", "Systems thinking"]

card_thumbnail: images/embedded-automate-panel/hero.jpg   # same screenshot as the case study hero
card_context: "HubSpot · Workflow automation · 2026"
card_summary: "Led design and co-led strategy for HubSpot's Automate panel. 72% of the workflows customers built used features new to Starter, and AI-recommended ones went live at 2× the rate."

page_overview: "Small business customers were leaving HubSpot because they couldn't automate the work they needed, and the automation they had was scattered and hard to find. We built one Automate panel that opens from the pages they already work in, with AI recommendations that show them where to start."
page_hero_fallback: images/embedded-automate-panel/hero.jpg
page_metrics:
  - value: "3×"
    label: "increase in automation discovery when we added an Automate button to the deal page (A/B test)"
  - value: "45%"
    label: "of AI-recommended workflows went live, twice the rate of starting from a blank page"
  - value: "72%"
    label: "of panel workflows used automation Starter customers never had before"
page_role_summary: "Lead product designer · Co-led vision with PM"
page_timeline: "Feb – Oct 2026 (beta July 23, launched to all Starter customers July 28–30, iterated through October)"
page_shipped_to: "HubSpot Starter"
page_chapters:
  - { id: context,  label: "Context",      headline: "Starter customers are small teams with little time to learn new tools" }
  - { id: problem,  label: "Problem",      headline: "Automation for Starter customers was scattered and hard to find" }
  - { id: strategy, label: "Strategy",     headline: "We moved automation onto the pages people already use" }
  - { id: research, label: "Concept validation", headline: "Customers backed the direction and showed us what was missing" }
  - { id: decision, label: "Design direction", headline: "Stakeholders and my team disagreed on the builder, so we tested both" }
  - { id: solution, label: "Final design",     headline: "Automation now lives on the pages people already use, written as plain sentences" }
  - { id: impact,   label: "Impact",       headline: "Most workflows built in the panel used features Starter didn't have before" }

filter_skills: ["Strategy", "Research", "AI and LLM design", "Interaction design", "Prototyping", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - Top of page layout: context line, title, page_overview (in the spot the old subtitle used), focus tags, hero, then a full-width Results row with the three page_metrics side by side (number above label), then My role, Timeline and Shipped to below. page_subtitle and page_problem are retired; remove the subtitle and the "The problem" block.
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption
-->

<!-- ============ CASE STUDY PAGE LAYOUT ============
  1. Top of page: title + page_overview + focus + hero, then a full-width Results row, then role/timeline/shipped to
  1b. "My role" (unnumbered) comes right after the top section, before 01 Context
  2. Full-story chapters (the body below). Each chapter: "## NN · Label {#id}" then "### Headline".
     Labels/headlines must match page_chapters.
  3. Reflection (unnumbered, last)
  Pull quotes: a blockquote (">") is a pull quote for people scanning the page. It repeats a customer
  quote that already appears in the text; it never replaces it. Last line of the blockquote = attribution.
  Max one per chapter (Design direction uses a pair to show the split).
  Nothing below this line appears on the home page card.
=================================================== -->

## My role {#role}

I led design for the Automate panel and co-led the vision with my PM. I worked with six front-end and back-end engineers, and with partner product teams who reviewed the design and placement of the panel on their pages.

I owned the interaction and visual design, from the first concepts in Lovable to the final specs in Figma. I also ran the research, wrote the framework for how AI recommendations explain themselves, and built the rulebook and agent skill that write each automation's sentence.

I started on the project in February 2026. The panel went to beta on July 23 and launched to all Starter customers by July 30, and I kept improving it through October.

## 01 · Context {#context}
### Starter customers are small teams with little time to learn new tools

HubSpot Starter is the entry-level paid plan, used by more than 150,000 customers, mostly founders and early hires at companies with 1 to 25 people. They’re wearing a lot of hats, and their attention is on finding customers and growing the business. Learning a tool like HubSpot, and automation in particular, feels like a big investment of time they don’t have. What they need is simple: leads that don’t fall through the cracks, deals that get followed up on, and tasks that get created without doing it manually.

## 02 · Problem {#problem}
### Automation for Starter customers was scattered and hard to find

Starter customers didn't have access to a central Workflows app. Instead, their automation experience was scattered across five different patterns. Each one had its own UI, its own entry point, and its own permissions. Some lived in settings, some lived inside individual apps, and some weren't visible anywhere. One customer described finding the automations tied to their records as "a little bit of an Easter egg hunt." Before this project, my team built a home page for automation that pointed customers to all of these tools. It helped them find automation, but it couldn't change how scattered the tools behind it were.

> "A little bit of an Easter egg hunt."
>
> Customer, describing how they found existing automations

Automating a simple task meant leaving your work to find the right screen, figuring out how that screen worked, and then coming back later to check what was running. Even our own teams had trouble keeping track of where automations lived. Adoption stayed low, and Starter customers who couldn't get what they needed were leaving to find other tools.

<!-- carousel -->
![Our audit of every automation surface in HubSpot, from pipeline settings to rulesets to sequences](images/embedded-automate-panel/problem-1.jpg)
![A few of those patterns as customers saw them: forms, deal pipelines, privacy settings, quotes, and the prospecting agent](images/embedded-automate-panel/problem-2.jpg)
<!-- /carousel -->

## 03 · Strategy {#strategy}
### We moved automation onto the pages people already use

My PM and I started with a brainstorm to define the goal for the project and how we might reach it. Our goal was to give Starter customers automation that was easy to find and easy to start, so they could stop doing repetitive work manually and wouldn't need to leave HubSpot for other tools.

The idea that shaped how we'd get there was that they're all workflows. Every embedded automation, wherever it showed up, could be backed by a real workflow. That meant someone could start with something simple on a deal page and later open the same automation in the full Workflows app without rebuilding it.

From there I proposed a single Automate experience that would look and work the same on every page where people already do their work. AI-generated recommendations, based on how each customer used their account, would show them where to start.

<!-- carousel -->
![The full brainstorm board](images/embedded-automate-panel/strategy-1.jpg)
![Core problems and what customers needed](images/embedded-automate-panel/strategy-2.jpg)
![The new approach: every embedded automation is a workflow](images/embedded-automate-panel/strategy-3.jpg)
![The vision for the whole system: embedded experience, unified canvas, unified management, and agents](images/embedded-automate-panel/strategy-4.jpg)
<!-- /carousel -->

## 04 · Concept validation {#research}
### Customers backed the direction and showed us what was missing

We tested the idea in two steps before building the panel. The first was about where the Automate button would live. The deal records page belonged to another team, who had been simplifying the record pages by moving buttons into menus to cut clutter. They worried a new button would add clutter without enough people getting value from it, and saw a rise in clicks as a vanity metric that wouldn't show customers found it useful.

So we ran an A/B test that moved the Automate button from settings onto the deal records page. Discovery went up 3x, and activation, meaning customers created a workflow, went up 2x. The result was statistically significant. The activation result showed that people who found the button went on to build automations, and we used it to show the team that owned the page, and their leadership, that the button was worth the space.

We then tested our first node and card design concept for the Automate panel with 12 customers, to check whether the new builder was easy to understand and use. Having automation right on the page made sense to them, and pre-filling the trigger from the record they were viewing made the biggest difference. One person said, "It's remembered all the context I've gone through. I haven't got to reselect or hunt for it."

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

One finding changed our plans: recommendations felt like ads unless they fit what the person was doing and explained why they mattered. That led to the recommendation framework in the final design.

## 05 · Design direction {#decision}
### Stakeholders and my team disagreed on the builder, so we tested both

Partner teams and leadership thought the builder looked too technical, and that writing each automation as a plain sentence ("When a deal moves to Closed Won, create a task for the deal owner") would make it easier. My team didn't think rewording triggers and conditions would make them easier to understand. We wanted to build on the node-and-card pattern people already knew from the Workflows app, so it would be easier to learn and customers who upgraded to Pro would find the full app familiar. Our first brainstorm also listed the downsides of sentences: lots of custom UI to build, and they might not translate well.

![Early pros and cons: sentence-style builder vs. AI-first creation](images/embedded-automate-panel/pros-cons.jpg)
<!-- IMAGE: brainstorm pros/cons board (unnamed-11) -->

![Three builder styles we explored, rules, sentences, and workflow nodes, each in a split or full view](images/embedded-automate-panel/explorations.jpg)

We took the stakeholders' feedback and built two Lovable prototypes to test both concepts with customers and see whether one was actually easier to use. The results were split. People who liked the sentence version said it felt "less like programming and more like just editing a Word doc." People who liked the node and canvas version said, "Makes me feel like I am building a workflow. Nodes are familiar."

> "Less like programming and more like just editing a Word doc."
>
> Customer who preferred the sentence version

> "Makes me feel like I am building a workflow. Nodes are familiar."
>
> Customer who preferred the node and canvas version

The test also showed something I didn't expect: the builder's design changed how people used AI. In the sentence version, people typed their changes to the AI. In the node and canvas version, they edited the cards directly.

![The sentence version and the node and canvas version, side by side as tested](images/embedded-automate-panel/research-styles.jpg)
<!-- IMAGE: the two tested prototypes side by side -->

With customers split, we went with the sentence version the stakeholders favored, and I led its visual design from there.

I started by exploring how the sentences should look. I tried a few builder layouts, from plain sentences to each step in its own card, and several styles for the parts people could edit, including tinted chips, bold underlined text, and dashed outlines for empty fields.

<!-- carousel -->
![Builder layout: plain sentences with no containers](images/embedded-automate-panel/builder-1.jpg)
![Builder layout: each step in its own card](images/embedded-automate-panel/builder-2.jpg)
![Builder layout: connected cards on a gray background](images/embedded-automate-panel/builder-3.jpg)
![Token styles: tinted chips colored by action type, compared with bold underlined text](images/embedded-automate-panel/tokens-1.jpg)
![Token styles: a single accent color, compared with dashed outlines on empty fields](images/embedded-automate-panel/tokens-2.jpg)
<!-- /carousel -->

My biggest concern had been scale, since every action needs its own sentence. So I built a rulebook and an agent skill that read an action's definition (its field labels, input order, and dependencies) and write its sentence automatically, for every existing and future action. The definition decides the structure, and the skill only handles the grammar.

Translation was the tradeoff we accepted. Each sentence follows the order of the fields in the form, so translators can change the words but can't reorder them. In languages with a different word order, some sentences read less naturally.

## 06 · Final design {#solution}
### Automation now lives on the pages people already use, written as plain sentences

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

Once the sentence builder was settled, we finalized the visual and interaction design around our original goal: making automation easy to find and easy to start.

We created a globally recognizable button that could be added to any app, and it passes that app's context into the Automate panel. Customers can start from suggestions based on that context and their team's activity, or create an automation from scratch or from a template. Picking one fills in the trigger based on where they opened the panel. Each automation reads as a sentence with the editable parts highlighted, so they can change a field in place, pull in data from the trigger, or ask the assistant beside it to make the change. Automations already set up for that page are listed below the suggestions.

Because recommendations felt like ads in research, I wrote a framework for how they explain themselves. Each one says what it will do for the business, never why HubSpot picked it. Accounts with enough activity see real evidence, like "28x this week deal owners were manually assigned," and newer accounts get suggestions that teach good habits instead.

The panel went to beta on July 23, 2026, and reached every Starter account by July 30.

## 07 · Impact {#impact}
### Most workflows built in the panel used features Starter didn't have before

Starter customers had been leaving because HubSpot couldn't automate the work they needed. After launch, 72% of the workflows built in the panel used features that weren't available on Starter before.

- 44K Starter accounts clicked Automate in the first 11 weeks, which is more than 1 in 4 Starter customers.
- About 1 in 3 of the 3,663 workflows that about 2,000 accounts started in the panel went live.

Workflows that started from an AI recommendation went live 45% of the time, compared with only 23% of workflows built from scratch.

We built the panel so other teams could reuse it, and Agent Hub Starter did. It launched on September 21 with the panel as its builder, and gave Starter customers one place to create and manage all their workflows for the first time. Weekly workflows turned on went from about 100 to about 340 in the weeks after.

## Reflection {#reflection}
### What I'd do differently

We looked at much more than ease of use. Our brainstorm weighed build time, scalability, and translation. But we didn't make that case strongly enough. If I'd laid out the pros, cons, and tradeoffs of each direction clearly for stakeholders, the conversation would have been about those tradeoffs.

I'd also test more ideas, and test them sooner. Putting several directions in front of customers early would have given everyone the same evidence to work from.

Once we committed to the sentence version, my job was to make it work. The scaling problem I'd worried about is what led me to build the rulebook and skill.

