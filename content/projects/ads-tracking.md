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
focus: ["Marketing tools"]

card_thumbnail: images/ads-tracking/card-screen.jpg   # card.jpg cropped to the screenshot, no cream border
card_context: "HubSpot · Ads tool · 2020"
card_summary: "Led design for HubSpot Ads tracking errors, from research through launch. In the months after release, the number of tracking errors dropped by about 50%."

page_subtitle: "Tracking errors gathered on the ads page marketers already check, grouped by type, with clear steps to fix each one, and shown only for ads that are still running."
page_problem: "Marketers couldn't see all the tracking errors on their ads, didn't know what they meant or how to fix them, and got alerts on ads that were no longer running."
page_hero_fallback: images/ads-tracking/hero-screen.jpg   # hero.jpg cropped to the screenshot, no cream border
page_metrics:
  - value: "~50%"
    label: "fewer tracking errors in the months after release"
  - value: "16 → 3"
    label: "monthly support tickets about ad tracking, November 2020 to January 2021"
  - value: "224"
    label: "customers surveyed to set the satisfaction baseline we'll measure against"
page_role_summary: "Product designer · HubSpot Ads"
page_shipped_to: "All HubSpot customers"
page_chapters:
  - { id: context,  label: "Context",          headline: "Marketers use HubSpot Ads to show what their ad spend brings in" }
  - { id: problem,  label: "Problem",          headline: "Customers couldn't tell when tracking was broken or how to fix it" }
  - { id: strategy, label: "Strategy",         headline: "We set out to put every error in one place and explain how to fix it" }
  - { id: decision, label: "Design direction", headline: "I worked with another designer on a shared error pattern and we rewrote every error message" }
  - { id: solution, label: "Final design",     headline: "Each part of the new design answers one of the problems we found" }
  - { id: impact,   label: "Impact",           headline: "Errors dropped by about half in the months after release" }

filter_skills: ["Research", "Interaction design", "Visual design", "Cross-team leadership"]
---

<!--
  NOTES FOR THE SITE BUILD
  - Carousels: images between the 'carousel' and '/carousel' comment markers are one carousel; each alt text is that slide's caption.
  - This page has six numbered chapters (no Concept validation), no timeline field, and no Reflection, by Jason's choice.
  - Metric sources: "about 50%" is total tracking errors from product analytics, Oct 2020 to Jan 2021 (Jan was likely a partial month). 16 → 3 is adsTracking support tickets by month, Nov 2020 to Jan 2021. 224 is the satisfaction survey baseline. All come from Jason's deck, not a live dashboard.
-->

## My role {#role}

I was the product designer for this redesign, working with my product manager and six front-end and back-end engineers. A product expert helped us dig into support tickets, a user researcher worked with me on the research, and I partnered with another designer who was solving a similar error problem in a different part of HubSpot.

I owned the design of the new tracking experience, from research planning through the final design. I worked with our researcher on the research plan, ran the analysis of the survey results, and led the iterations and the content audit of every error message.

## 01 · Context {#context}
### Marketers use HubSpot Ads to show what their ad spend brings in

For marketers, being able to measure their work is a big part of the job. It's how they show the business they're helping it grow. For advertising, that means knowing how many leads their ads bring in and what return they're getting on what they spend.

HubSpot Ads connects a customer's Facebook, Instagram, LinkedIn and Google ad accounts to HubSpot. To connect a contact back to the ad they came from, HubSpot adds tracking parameters to each ad's link. When that works, marketers see contacts, deals and ROI right next to their spend. When it doesn't, the ad shows zero contacts no matter how many people it brought in, and the marketer has no way to prove what it was worth.

## 02 · Problem {#problem}
### Customers couldn't tell when tracking was broken or how to fix it

There was already a solution for tracking errors, so we started by learning what was wrong with it. In the old design, each error showed up as a small "Alert" label in an ad's contacts column. To see what it meant, you had to hover over it, one ad at a time.

![The old design: an alert in the contacts column, explained only on hover](images/ads-tracking/problem-1.jpg)

We used three methods to understand what customers were running into. My PM and our product expert went through the support tickets, and I worked with our researcher on a plan that paired a satisfaction survey with usability testing.

The support tickets showed that most of the tracking volume came from customers seeing alerts on ads that were no longer active. In the survey, 29% of the 224 customers who answered were unhappy with tracking and 45% felt neutral. When I grouped their comments, the most common pattern was that it was unclear what the issue was and how to resolve it. Others asked why they were still seeing errors for campaigns they'd deleted.

> "Doesn't tell me how to fix them."
>
> Customer, satisfaction survey

In usability testing with five customers, we saw the same patterns, plus one more. Four of the five had a hard time finding all the errors affecting their ads, because they had to move through campaigns and ads to find each one.

<!-- carousel -->
![What we learned from support tickets, the survey and usability testing](images/ads-tracking/problem-2.jpg)
![Survey results: 26% happy, 45% neutral, 29% unhappy out of 224 customers](images/ads-tracking/problem-3.jpg)
![Survey comments grouped by theme, with not knowing how to fix errors as the largest group](images/ads-tracking/problem-4.jpg)
<!-- /carousel -->

## 03 · Strategy {#strategy}
### We set out to put every error in one place and explain how to fix it

The research left us with three problems. Customers had a hard time seeing how many errors they had, it was unclear what each issue was and how to resolve it, and they were getting alerts on ads that were no longer active.

Our goal was to make it easier for customers to learn when they weren't measuring their ads successfully, and to give them ways to fix the issues that came up. The idea was to stop treating errors as something you found ad by ad. Instead, we'd bring them all into one place, explain each one in plain language, and stop showing errors that no longer mattered.

## 04 · Design direction {#decision}
### I worked with another designer on a shared error pattern and we rewrote every error message

We went back to the drawing board on how to tell customers their ads had tracking issues and give them an easy way to resolve them. Another designer was solving a similar problem in a different part of HubSpot, so we worked together on a common pattern. That way customers would get the same experience for errors as they moved between different parts of the product.

I explored a panel that listed every error in one place. The iterations looked at how to group errors, including splitting the ones customers could fix from the ones they couldn't, and how to show each step of a fix, from refreshing tracking to confirming it worked.

![Iterations on the errors panel, exploring groups and fix states](images/ads-tracking/direction-1.jpg)

Since customers didn't understand what the errors meant, we also did a full content audit of every error message and rewrote them. Each one now follows the same structure: what's wrong, and then either how to fix it in HubSpot, how to fix it in the ad network, or a plain note that it can't be fixed and can be dismissed.

![The content audit: each error's old label and text next to the rewrite](images/ads-tracking/direction-2.jpg)

## 05 · Final design {#solution}
### Each part of the new design answers one of the problems we found

- Customers had a hard time seeing how many errors they had, so every error now rolls up to a single count on the ads page, with one place to review and resolve them all.
- It was unclear what each issue was, so errors are grouped by category with a count for each, which makes similar issues easier to understand and fix together.
- Each error explains what went wrong and how to fix it. Errors that can't be fixed say so and can be dismissed, so they stop showing up.
- Customers got alerts on ads that were no longer running, so inactive ads no longer show any errors.

<!-- carousel -->
![The ads page shows a total count of tracking errors, with a link to view them all](images/ads-tracking/final-1.jpg)
![The errors panel groups errors by type, and each one explains how to fix it or that it can't be fixed](images/ads-tracking/final-2.jpg)
<!-- /carousel -->

## 06 · Impact {#impact}
### Errors dropped by about half in the months after release

Customers had been getting errors they didn't understand, including on ads that weren't running anymore. In the months after release, the number of tracking errors dropped by about 50%, which met the goal we set before launch.

Before release we set three goals, and planned to measure them the same way we'd researched the problem:

- Cut the total number of tracking errors by 50%.
- Reduce support volume about tracking by 30%.
- Increase customer happiness with tracking by 20%.

Support tickets about ad tracking also went down, from 16 in November 2020 to 3 in January 2021. It's still too early to say whether that drop comes from the redesign or something else, so we're keeping an eye on it.

![Product analytics from October 2020 to January 2021](images/ads-tracking/impact-1.jpg)
![Support tickets by topic, November 2020 to January 2021](images/ads-tracking/impact-2.jpg)

We plan to run the satisfaction survey again and compare it to the baseline from our research. Until then, the drop in errors and the early fall in support tickets are the signals that tracking got easier for customers.
