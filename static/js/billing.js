function addRow() {
    const div = document.createElement("div");
    div.innerHTML = `
        <input type="text" name="product_id" placeholder="Product ID" required>
        <input type="number" name="quantity" placeholder="Quantity" required>
    `;
    document.getElementById("products").appendChild(div);
}