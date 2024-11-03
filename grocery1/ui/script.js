document.addEventListener("DOMContentLoaded", function() {
    fetch('/getProducts')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector("#productsTable tbody");
            tableBody.innerHTML = '';
            data.forEach(product => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${product.idproducts}</td>
                    <td>${product.productName}</td>
                    <td>${product.uom_id}</td>
                    <td>${product.Rate}</td>
                    <td>${product.uom_name}</td>
                    <td><button onclick="deleteProduct(${product.idproducts})">Delete</button></td>
                `;

                tableBody.appendChild(row);
            });
        });
});

function deleteProduct(productId) {
    fetch(`/deleteProduct/${productId}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            location.reload();
        } else {
            alert("Error: " + data.error);
        }
    });
}
