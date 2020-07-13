# Contributors Guide for the Python companion to *Statistical Thinking for the 21st Century*

Welcome to the this project!
We're excited you're here and want to contribute.

The goal of this project is to develop a fully Pythonic companion to the [core statistical text](https://statsthinking21.github.io/statsthinking21-core-site/), in parallel with the in-progress [R companion](https://github.com/statsthinking21/statsthinking21-R).

Any contributions to this project are welcome, from flagging minor typos to developing entirely new chapters. 

If you are experienced with the use of Git/Github for collaborative projects, you can jump to the [Technical Guidelines](#Technical-guidelines) section below.

## Practical guide to submitting your contribution

These guidelines are designed to make it as easy as possible to get involved.
If you have any questions that aren't discussed below,
please let us know by opening an [issue][link_issues]!

Before you start, you'll need to set up a free [GitHub][link_github] account and sign in.
Here are some [instructions][link_signupinstructions].

Already know what you're looking for in this guide? Jump to the following sections:

* [Joining the conversation](#joining-the-conversation)
* [Contributing through Github](#contributing-through-github)
* [Understanding issues](#understanding-issues)
* [Making a change](#making-a-change)
* [Structuring contributions](#fMRIPrep-coding-style-guide)
* [Licensing](#licensing)
* [Recognizing contributors](#recognizing-contributions)

## Joining the conversation

Discussions regarding the content and structure of the book take place via Github [issues][link_issues]. We actively monitor this space and look forward to hearing from you with any questions or suggestions.

## Contributing through GitHub

[git][link_git] is a really useful tool for version control.
[GitHub][link_github] sits on top of git and supports collaborative and distributed working.

If you're not yet familiar with `git`, there are lots of great resources to help you *git* started!
Some of our favorites include the [git Handbook][link_handbook] and
the [Software Carpentry introduction to git][link_swc_intro].

On GitHub, You'll use [Markdown][markdown] to chat in issues and pull requests.
You can think of Markdown as a few little symbols around your text that will allow GitHub
to render the text with a little bit of formatting.
For example, you could write words as bold (`**bold**`), or in italics (`*italics*`),
or as a [link][rick_roll] (`[link](https://youtu.be/dQw4w9WgXcQ)`) to another webpage.

GitHub has a really helpful page for getting started with
[writing and formatting Markdown on GitHub][writing_formatting_github].

## Understanding issues

Every project on GitHub uses [issues][link_issues] slightly differently. The following outlines how the *statsthinking21* developers think about these tools.

**Issues** are individual pieces of work that need to be completed to move the project forward.
A general guideline: if you find yourself tempted to write a great big issue that
is difficult to describe as one unit of work, please consider splitting it into two or more issues.

Issues are assigned [labels](#issue-labels) which explain how they relate to the overall project's goals and immediate next steps.

### Issue Labels

The current list of issue labels are [here][link_labels] and include:

* [![Good first issue](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/good%20first%20issue)][link_firstissue] *These issues contain a task that is amenable to new contributors because it doesn't entail a steep learning curve.*

    If you feel that you can contribute to one of these issues, we especially encourage you to do so!

* [![Bug](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/bug)][link_bugs] *These issues point to problems in the code.*

    If you find a new bug, please give as much detail as possible in your issue,
    including steps to recreate the error.
    If you experience the same bug as one already listed,
    please add any additional information that you have as a comment.

* [![Invalid](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/invalid)][link_bugs] *These issues point to conceptual or statistical errors in the text.*

    If you find a conceptual or statistical problem with the text, please note its line number, describe the rationale for your report, and suggest a fix if possible.

* [![Typo](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/typo)][link_bugs] *These issues point to typographic errors in the text.*

    If you find a new typo, please note its line number, and also note the recommended correction.

* [![New chapter](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/new%20chapter)][link_enhancement] *These issues are proposing a new chapter.*

    If you wish to propose a new chapter, please describe your rationale, and how it would fit with the existing chapters.  If possible, provide an outline of chapter subtopics.

* [![New section](https://img.shields.io/github/labels/statsthinking21/statsthinking21-python/new%20section)][link_enhancement] *These issues are proposing a new section to an existing chapter.*

    If you wish to propose a new section for an existing chapter, please describe your rationale, the topics that you think it should address, and how it would fit into the existing chapter.  

## Making a change

We appreciate all contributions to this book,
but those accepted fastest will follow a workflow similar to the following:

1. **Comment on an existing issue or open a new issue referencing your addition.**<br />
  This allows other members of the development team to confirm that you aren't
  overlapping with work that's currently underway and that everyone is on the same page
  with the goal of the work you're going to carry out.<br />
  [This blog][link_pushpullblog] is a nice explanation of why putting this work in up front
  is so useful to everyone involved.
  
1. **[Fork][link_fork] the [book repository][link_pybookrepo] to your profile.**<br />
  This is now your own unique copy of the book source.
  Changes here won't affect anyone else's work, so it's a safe space to explore edits to the code!
  
1. **[Clone][link_clone] your forked book repository to your machine/computer.**<br />
  While you can edit files [directly on github][link_githubedit], sometimes the changes
  you want to make will be complex and you will want to use a [text editor][link_texteditor]
  that you have installed on your local machine/computer.
  (One great text editor is [vscode][link_vscode]).<br />  
  In order to work on the code locally, you must clone your forked repository.<br />  
  To keep up with changes in the main book repository,
  add the ["upstream" book repository as a remote][link_addremote]
  to your locally cloned repository.  
    ```Shell
    git remote add upstream https://github.com/statsthinking21/statsthinking21-python.git
    ```
    Make sure to [keep your fork up to date][link_updateupstreamwiki] with the upstream repository.<br />  
    For example, to update your master branch on your local cloned repository:  
      ```Shell
      git fetch upstream
      git checkout master
      git merge upstream/master
      ```

1. **Create a [new branch][link_branches] to develop and maintain the proposed code changes.**<br />
  For example:
    ```Shell
    git fetch upstream  # Always start with an updated upstream
    git checkout -b fix/bug-1222 upstream/master
    ```
    Please consider using appropriate branch names as those listed below, and mind that some of them
    are special (e.g., `doc/` and `docs/`):
      * `fix/<some-identifier>`: for bugfixes
      * `enh/<feature-name>`: for new features
 
1. **Make the changes you've discussed, following the [style guide for Python code](https://www.python.org/dev/peps/pep-0008/).**<br />
  Try to keep the your changes focused: it is generally easy to review changes that address one new section or bug fix at a time.
  Once you are satisfied with your local changes, [add/commit/push them][link_add_commit_push]
  to the branch on your forked repository.

1. **Submit a [pull request][link_pullrequest].**<br />
   A member of the development team will review your changes to confirm
   that they can be merged into the main code base.<br />
   Pull request titles should begin with a descriptive prefix
   (for example, `FIX: Correct error in computation of standard deviation`):  
     * `ENH`: enhancements, such as new text or code ([example][enh_ex])
     * `FIX`: bug or typo fixes ([example][fix_ex])
     * `TST`: new or updated tests ([example][tst_ex])
     * `STY`: style changes ([example][sty_ex])
     * `REF`: refactoring existing code ([example][ref_ex])
     * `CI`: updates to continous integration infrastructure ([example][ci_ex])
     * `MAINT`: general maintenance ([example][maint_ex])
     * For works-in-progress, add the `WIP` tag in addition to the descriptive prefix.
       Pull-requests tagged with `WIP:` will not be merged until the tag is removed.

1. **Have your PR reviewed by the developers team, and update your changes accordingly in your branch.**<br />
   The reviewers will take special care in assisting you address their comments, as well as dealing with conflicts
   and other tricky situations that could emerge from distributed development.

## Technical guidelines

The (currently proposed) technical plan for the book is as follows. 

1. The code should be written in pure Python, targeting version 3.7 or greater.  All code should follow the [Python code style guide [PEP8]](https://www.python.org/dev/peps/pep-0008/), and should pass the [flake8](https://flake8.pycqa.org/en/latest/) style checker before submission.

1. The python file for each chapter will be named *chapter-<*topic*>.py*.  In principle, the chapters should coordinate with those in the [core text](https://statsthinking21.github.io/statsthinking21-core-site/); if one wishes to break this rule, then please raise an issue for discussion.  Any additional files (e.g. those defining utility functions) should be placed with the *utils* directory, and preferably named with the chapter topic in the name (e.g. "chapter-topic-utils.py").

1. The chapters files should be written using [Jupytext](https://github.com/mwouts/jupytext), which allows one to generate a jupyter notebook from a pure Python file, using the *percent* format in which cells are delimited with a commented %%. This decision was made in order to simplify the use of version control on the code; when using plain Jupyter notebooks, the metadata is saved in the file such that the file contents change every time the notebook is executed, making it very difficult to determine the relevant changes.  

1. The chapter files will be automatically converted to standard Jupyter notebooks using Jupytext using continuous integration.

1. The book will be generated using [jupyter-book](https://jupyterbook.org/intro.html), which renders the jupyter notebooks to html.

*TBD*: Identify additional style issues regarding the structure of the notebooks.  

## Recognizing contributions

We welcome and recognize all contributions regardless their size, content or scope:
from documentation to testing and code development.
You can see a list of current developers and contributors in our [zenodo file][link_zenodo].
Before every release, a new [zenodo file][link_zenodo] will be generated.
After the first draft is complete, we will create an update script that will also sort creators and contributors by
the relative size of their contributions, as provided by the `git-line-summary` utility
distributed with the `git-extras` package.
Last positions in both the *creators* and *contributors* list will be reserved to
the project leaders.
These special positions can be revised to add names by punctual request and revised for
removal and update of ordering in an scheduled manner every two years.
All the authors enlisted as *creators* participate in the revision of modifications.

### Creators

Creators are members of a the team who have been responsible for  _establishing and/or driving the project_.
Names and contacts of all creators are included in the
[``.maint/creators.json`` file](https://github.com/statsthinking21/statsthinking21-python/blob/master/.maint/developers.json)
Examples of steering activities that _drive the project_ are: actively participating in the development of new content, helping with the design of the project, and providing resources (in the broad sense, including funding).

### Contributors

Contributors listed in the
[``.maint/contributors.json`` file](https://github.com/statsthinking21/statsthinking21-python//blob/master/.maint/contributors.json)
actively help or have previously helped the project in a broad sense: writing code or text,
proposing new features, and finding bugs.
If you are new to the project, don't forget to add your name and affiliation to the list
of contributors there!

Contributors who have contributed at some point to the project but wish to drop out of the project are listed in the [``.maint/former.json`` file](https://github.com/poldracklab/fmriprep/blob/master/.maint/former.json).

## Licensing

This companion is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC-BY-NC).  While we are generally opposed to the use of non-commercial licenses, in this case it is necessary.  The core statistical text will be published by a commercial publisher as a low-cost paperback book, and this publisher reasonably requires that the open-source version be licensed to prevent other commercial reuse.  Because the companion texts may end up incorporating text from the core text, we must thus also license the companions according to CC-BY-NC as well.  A benefit of this is that contibutors do not need to worry about "contaminating" the companions with text from the core; in fact, it's perfectly ok to do so, as long as the license terms are upheld.

By contributing to this book,
you acknowledge that any contributions will be licensed under the same terms.  

## Thank you!

You're awesome. :wave::smiley:

<br>

*&mdash; Based on contributing guidelines from the [STEMMRoleModels][link_stemmrolemodels] and [fMRIprep][link_fmriprep] projects.*

[link_github]: https://github.com/
[link_fMRIPrep]: https://github.com/poldracklab/fmriprep
[link_pybookrepo]: https://github.com/statsthinking21/statsthinking21-python/
[link_signupinstructions]: https://help.github.com/articles/signing-up-for-a-new-github-account

[link_git]: https://git-scm.com/
[link_handbook]: https://guides.github.com/introduction/git-handbook/
[link_swc_intro]: http://swcarpentry.github.io/git-novice/

[writing_formatting_github]: https://help.github.com/articles/getting-started-with-writing-and-formatting-on-github
[markdown]: https://daringfireball.net/projects/markdown
[rick_roll]: https://www.youtube.com/watch?v=dQw4w9WgXcQ

[link_issues]: https://github.com/statsthinking21/statsthinking21-python/issues
[link_labels]: https://github.com/statsthinking21/statsthinking21-python/labels
[link_discussingissues]: https://help.github.com/articles/discussing-projects-in-issues-and-pull-requests

[link_bugs]: https://github.com/statsthinking21/statsthinking21-python/labels/bug
[link_firstissue]: https://github.com/statsthinking21/statsthinking21-python/labels/good%20first%20issue
[link_enhancement]: https://github.com/statsthinking21/statsthinking21-python/labels/enhancement

[link_pullrequest]: https://help.github.com/articles/creating-a-pull-request-from-a-fork
[link_fork]: https://help.github.com/articles/fork-a-repo/
[link_clone]: https://help.github.com/articles/cloning-a-repository
[link_githubedit]: https://help.github.com/articles/editing-files-in-your-repository
[link_texteditor]: https://en.wikipedia.org/wiki/Text_editor
[link_vscode]: https://code.visualstudio.com/
[link_addremote]: https://help.github.com/articles/configuring-a-remote-for-a-fork
[link_pushpullblog]: https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/
[link_branches]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/
[link_add_commit_push]: https://help.github.com/articles/adding-a-file-to-a-repository-using-the-command-line
[link_updateupstreamwiki]: https://help.github.com/articles/syncing-a-fork/
[link_stemmrolemodels]: https://github.com/KirstieJane/STEMMRoleModels
[link_zenodo]: https://github.com/statsthinking21/statsthinking21-python//blob/master/.zenodo.json
[link_update_script]: https://github.com/poldracklab/fmriprep/blob/master/.maintenance/update_zenodo.py
[link_devel]: https://fmriprep.readthedocs.io/en/latest/contributors.html
[link_fmriprep]: http://fmriprep.org
[link_bidsapps]: https://bids-apps.neuroimaging.io
[link_mattermost]: https://mattermost.brainhack.org/brainhack/channels/fmriprep
[link_aroma]: https://fmriprep.readthedocs.io/en/stable/workflows.html#ica-aroma

[enh_ex]: https://github.com/poldracklab/fmriprep/pull/1508
[fix_ex]: https://github.com/poldracklab/fmriprep/pull/1378
[tst_ex]: https://github.com/poldracklab/fmriprep/pull/1098
[doc_ex]: https://github.com/poldracklab/fmriprep/pull/1515
[sty_ex]: https://github.com/poldracklab/fmriprep/pull/675
[ref_ex]: https://github.com/poldracklab/fmriprep/pull/816
[ci_ex]: https://github.com/poldracklab/fmriprep/pull/1048
[maint_ex]: https://github.com/poldracklab/fmriprep/pull/1239