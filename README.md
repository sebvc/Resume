# My Resume Repo

Sebastian Villa Cuellar's Professional Resume Material with implemented Github Tracking

> Feel free to Fork and utilize anything as a template for your resume, just reference the [**My Usage**](#my-usage) and [**For You**](#for-you) sections below.

![---](https://github.com/sebvc/Resume/assets/90735870/78313136-8b1d-4cb4-ad42-71e3ed6ff5c1)

## Main Project Repository structure: [(Browse File Tree Here)](https://github.com/sebvc/Resume/)

<pre><code>📁Resume/
├──📝<a href="https://sebvc.github.io/Resume/sebvc_Resume.docx">sebvc_Resume.docx</a> # To Edit Resume
├──📄<a href="https://sebvc.github.io/Resume/sebvc_Resume.pdf">sebvc_Resume.pdf</a> # Shareable PDF 
└──🗃️<a href="https://github.com/sebvc/Resume/blob/main/sebvc_Resume.md">sebvc_Resume.md</a> # For Git Version Control Tracking
</code></pre>

<!-- ```sh
📁Resume/
├──📝sebvc_Resume.docx # To Edit Resume
├──📄sebvc_Resume.pdf # Shareable PDF 
└──🗃️sebvc_Resume.md # For Git Version Control Tracking
``` -->

[***Click Here to view my Resume Pdf***](https://sebvc.github.io/Resume/sebvc_Resume.pdf) or Paste [https://sebvc.github.io/Resume/sebvc_Resume.pdf](https://sebvc.github.io/Resume/sebvc_Resume.pdf) to your Browser.

Visit [https://github.com/sebvc/Resume](https://github.com/sebvc/Resume) to view Resume progression tracked on GitHub and explore the full Repo

---

## My Usage

1. **_Edit_** the master Resume document, a MS Word `.docx` file
2. **_Export_** to a `.pdf` document
3. **_Run_** the desired `convert.*` script or use the command line to convert the Word `.docx` file to the Markdown `.md` file and to have a text based resume to track changes with git
4. **_Commit_** and push all to GitHub Repository and GitHub Pages

### Convert Script 🪄💻

The Convert Scripts can be executed with Julia or Python in on the command line in the Resume Directory.

The scripts I provided are run with either:

- `julia .\scripts\convert.jl` (need [Julia](https://julialang.org/))
- `py .\scripts\convert.py` (need [Python](https://www.python.org/))
- `.\scripts\convert.ps1` (in PowerShell)


They both convert the file from from `.docx` to `.md` and insert a few styling lines to the new `.md` file. The variables in the script specify the name of the files it reads and produces.

> My MS Word document is composed of a full page table with many merged and split cells. I use **[pandoc](https://pandoc.org/)**, an open-source comandline document converter, to convert from `.docx` to `.md`. It's key to note that I convert it to github flavored markdown (gfm) that renders nicely on github, but converting it to any Markdown syntax or even a plain text files would function simmilarly for tracking changes with Git.

I use following command-line to convert my MS Word `.docx` file to a MultiMarkdown `.md` file:

> ```ps
> pandoc -f docx+styles -t gfm sebvc_Resume.docx -o sebvc_Resume.md -H ".\media\style_css_header.md"
> ```

I also preview the `.md` file on VSCode, so for formatting sake I add the following CSS Styling file to the head of the `.md` file and any images or icons rendered in the pdf are stored in the same `./media/` directory:

> ```html
> <head>
>  <link rel="stylesheet" href="media/style_block_insert.css">
> </head>
> ```

---

## For You

This Resume, and more specifically this Repo, is **Open-Source, _not_ Open-Contribution**, similar to [SQLite](https://www.sqlite.org/copyright.html) and [Litestream](https://github.com/benbjohnson/litestream/commit/a8d63b54aa5bd2d9639af01e1e0c2098a65b323a#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5R121).

I want people to freely be able to access and modify my Repo and my Resume as a resource and template to improve their own, but not directly affect/change my original Personal copy. That is the Reason for the [BSD 3-Clause License](./LICENSE.md), it is freely and easily permisive, but unless allowed by myself, my name must be removed from redistributions of the material.

I encourage you to Feel Free to leave suggestions, comments, and/or even endorsemnts in your own words, but any direct contributions (such as merges and Pull Requests) will most likely be ignored.

If you wish to enquire more (with questions or opportunities) please contact me thorugh any of the ways found at the top of my [Resume](./sebvc_Resume.md) or [Website](https://tx.ag/sebvc) and I will get back to you soon.

### Wiki Walkthrough Guide 📝🔗

To be implemented soon
