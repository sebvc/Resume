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