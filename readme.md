

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
- table-class/table-style: class for generated table/style for generated table
- tr-class/tr-style: class for generated tr/style for generated tr
- td-class/td-style: class for generated td/style for generated td
  
## Mobile or Desktop Attribute  

 - For mobile
``<separator mobile></separator>``
 - For desktop
``<separator table-class="hide"></separator>`` `

## Don't use TR with TD tag 
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
