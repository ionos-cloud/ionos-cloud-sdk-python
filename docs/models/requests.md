# Requests

## Properties

| Name | Type | Description | Notes |
| :--- | :--- | :--- | :--- |
| **id** | **str** | The resource's unique identifier | \[optional\] \[readonly\] |
| **type** | [**Type**](type.md) | The type of object that has been created | \[optional\] |
| **href** | **str** | URL to the object representation \(absolute path\) | \[optional\] \[readonly\] |
| **items** | [**list\[Request\]**](request.md) | Array of items in that collection | \[optional\] \[readonly\] |
| **offset** | **float** | the offset specified in the request \(or, if none was specified, the default offset of 0\) |  |
| **limit** | **float** | the limit specified in the request \(or, if none was specified, the default limit of 0\) |  |
| **links** | [**PaginationLinks**](paginationlinks.md) |  |  |

