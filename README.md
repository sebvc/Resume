# My Resume Repo
Sebastian Villa Cuellar's Professional Resume Material with implemented Github Tracking

>Feel free to Fork and utilize anything as a template for your resume, just reference the [**My Usage**](#my-usage) and [**For You**](#for-you) sections below.

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

1. Personally, I build and modify my resume with MS Word. 
2. I then export it to a PDF when I have a new itteration.
3. Then I use following Code Block to track MS Word `.docx` file changes with git. 
<blockquote>

```ps
pandoc -f docx -t markdown_mmd sebvc_Resume.docx -o sebvc_Resume.md 
```

</blockquote>


4. and then add I add the following to the head of the `sebvc_Resume.md` file:

<blockquote>

```html
<head>
  <link rel="stylesheet" href="media/style_block_insert.css">
</head>
```

</blockquote>

5. I stage and commit the three modified files to Github to update the remote version of my Resume that is used by [my website at tx.ag/sebvc](https://tx.ag/sebvc) and [LinkedIn](https://www.linkedin.com/in/sebvc/), and track my changes over time. 

---
## For You
This Resume, and more specifically this Repo, is **Open-Source, _not_ Open-Contribution**, similar to [SQLite](https://www.sqlite.org/copyright.html) and [Litestream](https://github.com/benbjohnson/litestream/commit/a8d63b54aa5bd2d9639af01e1e0c2098a65b323a#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5R121). 

I want people to freely be able to access and modify my Repo and my Resume as a template to improve their own, but not directly affect/change my original Personal copy. That is the Reason for the [BSD 3-Clause License](./LICENSE.md), it is freely and easily permisive, but unless allowed by myself, my name must be removed from redistributions of the material.

I encourage you to Feel Free to leave suggestions, comments, and/or even endorsemnts in your own words, but any direct contributions (such as merges and Pull Requests) will most likely be ignored.

If you wish to enquire more (with questions or opportunities) please contact me thorugh any of the ways found at the top of my [Resume](./sebvc_Resume.md) or [Website](https://tx.ag/sebvc) and I will get back to you soon.
