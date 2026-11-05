---
# Field prefixes say where each field appears:
#   (no prefix) = both the home page card and the case study page
#   card_       = home page project card only
#   page_       = case study page only
#   filter_     = not displayed; used for filtering

title: "Redesigning how HubSpot Ads reports tracking errors"
slug: ads-tracking
order: 3
featured: true
focus: ["Reporting", "Marketing"]

card_thumbnail: images/ads-tracking/card-screen.jpg   # card.jpg cropped to the screenshot, no cream border
card_context: "HubSpot · Ads tool · 2020"
card_summary: "Led design for HubSpot Ads tracking errors, from research through launch. In the months after release, the number of tracking errors dropped by about half."

page_overview: "When ad tracking broke, marketers couldn't prove what their spend brought in, and HubSpot's alerts were hard to find and didn't say how to fix anything. We brought every error onto the ads page marketers already check, with clear steps to fix each one."
page_hero_fallback: images/ads-tracking/hero-screen.jpg   # hero.jpg cropped to the screenshot, no cream border
page_metrics:
  - value: "~50%"
    label: "fewer tracking errors in the months after release"
  - value: "~80%"
    label: "fewer monthly support tickets about ad tracking"
page_role_summary: "Product designer · HubSpot Ads"
page_shipped_to: "All HubSpot customers"
page_chapters:
  - { id: context,  label: "Context",       headline: "Tracking is how marketers prove their ads are worth paying for" }
  - { id: problem,  label: "Problem",       headline: "Ads showed zero contacts, and the only clue was a label you had to hover over" }
  - { id: strategy, label: "Strategy",      headline: "We wanted customers to see every error at once instead of one ad at a time" }
  - { id: decision, label: "Key decisions", headline: "Another designer had the same problem, so we solved it once" }
  - { id: solution, label: "Final design",  headline: "Every error now shows up in one count and comes with a fix" }
  - { id: impact,   label: "Impact",        headline: "Tracking errors dropped by about half" }

filter_skills: ["Research", "Interaction design", "Visual design", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - Top of page layout: context line, title, page_overview (in the spot the old subtitle used), focus tags, hero, then a full-width Results row with the three page_metrics side by side (number above label), then My role, Timeline and Shipped to below. page_subtitle and page_problem are retired; remove the subtitle and the "The problem" block.
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption.
  - This page has six numbered chapters (no Concept validation), no timeline field, and no Reflection, by Jason's choice.
  - This page has two headline metrics, not three. Lay out the Results row with two side by side, and skip the Timeline row since there's no timeline field.
  - Key decisions (04) uses "####" subheads to separate its three decisions. Style them smaller than the chapter headline.
  - Metric sources: "about 50%" is total tracking errors from product analytics, Oct 2020 to Jan 2021 (Jan was likely a partial month). "About 80%" is adsTracking support tickets by month, 16 in Nov 2020 to 3 in Jan 2021 (an 81% drop; Jan was likely a partial month). All come from Jason's deck, not a live dashboard.
-->

## My role {#role}

I was the product designer for this redesign, working with my product manager and six front-end and back-end engineers. A product expert helped us dig into support tickets, a user researcher worked with me on the research, and I partnered with another designer who was solving a similar error problem in a different part of HubSpot.

I owned the design of the new tracking experience, from research planning through the final design. I worked with our researcher on the research plan, ran the analysis of the survey results, and led the iterations and the content audit of every error message.

## 01 · Context {#context}
### Tracking is how marketers prove their ads are worth paying for

Showing ROI was the main reason marketers managed their ads in HubSpot instead of in each ad network. It's how they show the business how many leads their ads bring in and what return they're getting on what they spend.

HubSpot Ads connects a customer's Facebook, Instagram, LinkedIn and Google ad accounts to HubSpot. To connect a contact back to the ad they came from, HubSpot adds tracking parameters to each ad's link. When that works, marketers see contacts, deals and ROI right next to their spend. When it doesn't, the ad shows zero contacts no matter how many people it brought in, and the marketer has no way to prove what it was worth.

## 02 · Problem {#problem}
### Ads showed zero contacts, and the only clue was a label you had to hover over

When tracking broke, customers lost the main reason to use HubSpot Ads, and they turned to support to find out what had gone wrong.

There was already a solution for tracking errors, so we started by learning what was wrong with it. In the old design, each error showed up as a small "Alert" label in an ad's contacts column. To see what it meant, you had to hover over it, one ad at a time.

![The old design: an alert in the contacts column, explained only on hover](images/ads-tracking/problem-1.jpg)

We used three methods to understand what customers were running into. My PM and our product expert went through the support tickets, and I worked with our researcher on a plan that paired a satisfaction survey with usability testing.

The support tickets showed that most of the tracking volume came from customers seeing alerts on ads that were no longer active. In the survey, only about 1 in 4 customers who answered were happy with tracking. When I grouped their comments, the most common pattern was that it was unclear what the issue was and how to resolve it. One customer wrote that it "doesn't tell me how to fix them." Others asked why they were still seeing errors for campaigns they'd deleted.

> "Doesn't tell me how to fix them."
>
> Customer, satisfaction survey

In usability testing with five customers, four of the five had a hard time finding all the errors affecting their ads, because they had to move through campaigns and ads to find each one.

<!-- carousel -->
![What we learned from support tickets, the survey and usability testing](images/ads-tracking/problem-2.jpg)
![Survey results: 26% happy, 45% neutral, 29% unhappy out of 224 customers](images/ads-tracking/problem-3.jpg)
![Survey comments grouped by theme, with not knowing how to fix errors as the largest group](images/ads-tracking/problem-4.jpg)
<!-- /carousel -->

That gave us our question: how might we help marketers catch and fix tracking problems on their own, so they can trust their ROI without contacting support?

## 03 · Strategy {#strategy}
### We wanted customers to see every error at once instead of one ad at a time

The research left us with three problems. Customers had a hard time seeing how many errors they had, it was unclear what each issue was and how to resolve it, and they were getting alerts on ads that were no longer active.

Our goal was to make it easier for customers to learn when they weren't measuring their ads successfully, and to give them ways to fix the issues that came up. The idea was to stop treating errors as something you found ad by ad. Instead, we'd bring them all into one place, explain each one in plain language, and stop showing errors that no longer mattered.

Before launch, we set three targets to measure it, using the same sources we'd used to research the problem: cut tracking errors in half, cut tracking support tickets by 30%, and raise satisfaction with tracking by 20%.

## 04 · Key decisions {#decision}
### Another designer had the same problem, so we solved it once

#### A shared error pattern

We went back to the drawing board on how to tell customers their ads had tracking issues and give them an easy way to resolve them. Another designer was solving a similar problem in a different part of HubSpot, so we worked together on a common pattern. That way customers would get the same experience for errors as they moved between different parts of the product.

I explored a panel that listed every error in one place. The iterations looked at how to group errors, including splitting the ones customers could fix from the ones they couldn't, and how to show each step of a fix, from refreshing tracking to confirming it worked.

![Iterations on the errors panel, exploring groups and fix states](images/ads-tracking/direction-1.jpg)

#### Rewriting every error message

Since customers didn't understand what the errors meant, we also did a full content audit of every error message and rewrote them. Each one now follows the same structure: what's wrong, and then either how to fix it in HubSpot, how to fix it in the ad network, or a plain note that it can't be fixed and can be dismissed.

![The content audit: each error's old label and text next to the rewrite](images/ads-tracking/direction-2.jpg)

#### Hiding errors on inactive ads

Support tickets showed that alerts on inactive ads drove most of the tracking support volume, so we stopped showing errors on any ad that isn't active.

## 05 · Final design {#solution}
### Every error now shows up in one count and comes with a fix

<!-- carousel -->
![The ads page shows a total count of tracking errors, with a link to view them all](images/ads-tracking/final-1.jpg)
![The errors panel groups errors by type, and each one explains how to fix it or that it can't be fixed](images/ads-tracking/final-2.jpg)
<!-- /carousel -->

With the shared error pattern and the rewritten messages in place, we finalized the design around our original goal: making it easy for customers to see when their ads aren't being tracked and how to fix it.

We brought every tracking error up to a single count at the top of the ads page, which opens one panel where customers can review and resolve them all.

Customers see the number of tracking errors above their campaigns, and each affected campaign is marked with a tracking error. Selecting View errors opens the panel, where errors are grouped by category with a count for each, so similar issues can be worked through together. Each error explains what's wrong and how to fix it, either in HubSpot or in the ad network. Errors that can't be fixed say so, and customers can dismiss them to a separate Dismissed tab.

## 06 · Impact {#impact}
### Tracking errors dropped by about half

Customers had been getting errors they didn't understand, including on ads that weren't running anymore, which put the main reason to use HubSpot Ads at risk. In the months after release, the number of tracking errors dropped by about half, which met our first target.

Support tickets about ad tracking also fell by about 80%, well past our 30% target, but it was too early to say how much of the drop came from the redesign.

![Product analytics from October 2020 to January 2021](images/ads-tracking/impact-1.jpg)
![Support tickets by topic, November 2020 to January 2021](images/ads-tracking/impact-2.jpg)

We didn't get to rerun the satisfaction survey, so that target was never measured. The drop in errors and the fall in support tickets are the signs we have that tracking got easier for customers.
