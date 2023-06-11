# Resume
Sebastian Villa Cuellar's Professional Resume Material

Main Project Repository structure:
```sh
📁Resume/
├──📝sebvc_Resume.docx # To Edit Resume
├──📄sebvc_Resume.pdf # Shareable PDF 
└──🗃️sebvc_Resume.md # For Git Version Control Tracking
```

[Click Here to view Resume Pdf](https://sebvc.github.io/Resume/sebvc_Resume.pdf) or Paste https://sebvc.github.io/Resume/sebvc_Resume.pdf to your Browser.
 
Visit https://github.com/sebvc/Resume to view Resume progression tracked on GitHub
  

---
## My Usage 
I use following Code Block to track MS Word `.docx` file changes with git. 
```ps
pandoc -f docx -t markdown_mmd sebvc_Resume.docx -o sebvc_Resume.md 
```
and then add I add the following to the head of the `sebvc_Resume.md` file:
```html
<head>
  <link rel="stylesheet" href="media/style_block_insert.css">
</head>
```

---
## For You
This Resume, and more specifically this Repo, is **Open-Source, _not_ Open-Contribution**, similar to [SQLite](https://www.sqlite.org/copyright.html) and [Litestream](https://github.com/benbjohnson/litestream/commit/a8d63b54aa5bd2d9639af01e1e0c2098a65b323a#diff-b335630551682c19a781afebcf4d07bf978fb1f8ac04c6bf87428ed5106870f5R121). 

I want people to freely be able to access and modify my Repo and my Resume as a template to improve their own, but not directly affect/change my original Personal copy. That is the Reason for the BSD 3-Clause License, it is freely and easily permisive, but unless allowed by myself, my name must be removed from redistributions of the material.

I encourage you to Feel Free to leave suggestions, comments, and/or even endorsemnts in your own words, but any direct contributions (such as merges and Pull Requests) will most likely be ignored.

If you wish to enquire more (with questions or opportunities) please contact me thorugh any of the ways found at the top of my [Resume](./sebvc_Resume.md) or [Website](https://tx.ag/sebvc) and I will get back to you soon.
