# Resume
Sebastian Villa Cuellar's Professional Resume Material

Use following Code Block to track word .docx file changes with git. 
```
pandoc -f docx -t markdown_mmd sebvc_Resume.docx -o sebvc_Resume.md 
```
and add the following to the .md file:
```
<head>
  <link rel="stylesheet" href="media/style_block_insert.css">
</head>
```