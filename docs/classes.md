# Classes
## Class 0

* Change container names in local.yml


## Class 3 Pagination

### Pagination snippet
  * Using include in **templates/stores/storechain_list.html** the 
  **templates/snippets/pagination_snippet.html**
### HTMX
* Add script tag to **templates/base.html**
```html
<script src="https://unpkg.com/htmx.org@1.6.1"
            integrity="sha384-tvG/2mnCFmGQzYC1Oh3qxQ7CkQ9kMzYjWZSNtrRZygHPDDqottzEJsqS4oUVodhW"
            crossorigin="anonymous"></script>
```
* Add eventListener to **templates/base.html** for csrf_token
```javascript
<script>
  document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
  })
</script>
```
