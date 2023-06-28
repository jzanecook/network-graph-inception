# network-graph-inception

You can see the initial run's results at [this link.](https://github.com/jzanecook/network-graph-inception/pull/1)

# e2b Demo First Impressions

[My Biggest Question](#my-biggest-question)

### Logging In
- Perfect execution of a GitHub sign-in, no issues throughout this entire process. Looking great!
- [Are you planning on supporting other third party sign-ins?](#are-you-planning-on-supporting-other-third-party-sign-ins)

### Setup
- The option to use a new or existing repository is a good move.
- The UI involved in telling the agent what to build is good, however:
	- It could use a more complex templating/preset scheme e.g. a search bar to "community presets" whenever you launch or a dropdown with more options.
	- While the open-ended markdown text area is a good move for more projects, being able to specify additional options to the agent in this (Step 2 of 3) page might be worthwhile, e.g. temperature, presence, flags for the agent.
	- Additionally, the editor itself doesn't seem to let you edit the markdown, but rather shows the text editor in the formatted view, this may hinder markdown editing especially if you're not using a template. See [Markdown Issues](#markdown-issues) for more on this subject.

### Deployment

> Great Work!
> I like the general UI design choices you've made! This modernized purplish hue is fairly common, but it's stylish and easy on the eyes. I would suggest adding a light mode, as some people do normally request such barbaric things, but I am not in that category.

- One of the initial "issues" I see is that my context is not scrolling to the newest log, e.g. after I click deploy and the agent has run its course I am still on the `Info: Initial prompt` section. I personally enjoy the Github Actions (or insert alternative CI/CD deployment here) flow where my view will follow the context of the actions taking place. I also notice that this doesn't quite match up with some of your previous screenshots. [Is there a reason this view couldn't be implemented with smol developer or is it just on the backburner for this release since you're pushing a demo out for people to see?](#is-there-a-reason-this-view-couldnt-be-implemented-with-smol-developer-or-is-it-just-on-the-backburner-for-this-release-since-youre-pushing-a-demo-out-for-people-to-see)
- I do wish the page linked off to the GitHub repository so that I could quickly go back and forth between them, with it having created a new repository I had to open GitHub and go find it.

### GitHub Flow
- The only thing really missing is a backlink to the e2b page for me to visit to view the logs in there. Being able to switch between e2b and github easily is a must.
- Another option would be to have a progress bar that shows whether it's still deploying or done, rather than individual comments.
- I see no issues with the PR/commit flow, it seems to be working well, as intended.

---

# Markdown Issues
1. The title given is being used in the prompts, but is keeping the formatting, I see in the logs for the prompt that it keeps the markdown formatting e.g. `MOST IMPORTANT OF ALL - the purpose of our app is # Network Graph Web Scraper`
2. The output (if the bot responded with markdown) seems to be normally formatted in triple quotes for multi line code comments. I notice that there is prompting to try to tell the agent to respond without those multi line comments, but I think that this method will be extremely unstable due to the majority of text-based code given to these LLMs to train will likely be in the form of medium-esque articles where that formatting is inherent. It's likely better to try and check the `result` string and take those quotes out with a regex, you could also potentially design a regex that could check if the `result` string includes more than code, e.g. if there were a code block as well as text outside of the code block, this could be used theoretically to re-run the command if needed, or take whatever the code block contains and put that into the file rather than the entire `result` string.

# Questions

### Are you planning on supporting other third party sign-ins?
- e.g. Google?
- It's not a must-have, but I just figured I'd ask since right now it's purely GitHub.

### Is there a reason this view couldn't be implemented with smol developer or is it just on the backburner for this release since you're pushing a demo out for people to see?
![something like this](https://media.discordapp.net/attachments/1118671037782040616/1120120560538624110/Screenshot_2023-06-18_at_3.38.29_PM.png?width=892&height=673)
- Although I'm sure that's just something you're planning on adding and is likely in a branch somewhere.
- Or was it a design demo, e.g. not actually implemented yet?

### My Biggest Question
# WHEN DAT SDK DROP!?!?!?
