
# Separator tag
``<separator>conteudo</separator>`` = ``<table><tr><td>conteudo</td></tr></table>`` with userful attributes



## Separator and attributes
```
<separator
table-class="" table-style=""
tr-class="" tr-style=""
td-class="" td-style="">
</separator>
```
  
## Mobile or desktop Attribute  

 - For mobile
``<separator mobile></separator>``
 - For desktop
``<separator table-class="hide"></separator>`` `

## Don't use TR tag 
```
# Use
<column>
  <row>
  content
  </row>
</column>

# instead of
<table>
  <tr>
    <td>content</td>
  </tr>
</table>
```

# Video tutorial
https://www.youtube.com/watch?v=BcMczxnwI_Q
