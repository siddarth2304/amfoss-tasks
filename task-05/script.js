// script.js

let cart = [];
let products = [];
const terminalOutput = document.getElementById('output');
const productsList = document.getElementById('products-list');
const cartItemsContainer = document.getElementById('cart-items');
const totalAmountElement = document.getElementById('total-amount');
const totalTaxElement = document.getElementById('total-tax');
const checkoutButton = document.getElementById('checkout-btn');
const thankYouMessage = document.getElementById('thank-you-message');
const mainPage = document.getElementById('main-page');
const checkoutPage = document.getElementById('checkout-page');

async function fetchProducts() {
    const res = await fetch('https://fakestoreapi.com/products');
    products = await res.json();
}

async function displayProducts() {
    await fetchProducts();
    products.forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
            <img src="${product.image}" alt="${product.title}">
            <h3>${product.title}</h3>
            <p>$${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productsList.appendChild(productCard);
    });
}

function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) {
        cart.push(product);
        logToTerminal(`Product "${product.title}" added to cart.`);
    } else {
        logToTerminal(`Product with ID ${productId} not found.`);
    }
}

function removeFromCart(productId) {
    const productIndex = cart.findIndex(p => p.id === productId);
    if (productIndex !== -1) {
        logToTerminal(`Product "${cart[productIndex].title}" removed from cart.`);
        cart.splice(productIndex, 1);
    } else {
        logToTerminal(`Product with ID ${productId} not found in cart.`);
    }
}

function logToTerminal(message) {
    const p = document.createElement('p');
    p.textContent = message;
    terminalOutput.appendChild(p);
    terminalOutput.scrollTop = terminalOutput.scrollHeight;
}

function executeCommand(command) {
    const [cmd, ...args] = command.toLowerCase().split(' ');

    switch (cmd) {
        case 'list':
            logToTerminal('Listing all products...');
            products.forEach(product => {
                logToTerminal(`${product.id}: ${product.title} - $${product.price}`);
            });
            break;
        case 'details':
            const product = products.find(p => p.id === parseInt(args[0]));
            if (product) {
                logToTerminal(`Details of Product ID ${product.id}:\nTitle: ${product.title}\nPrice: $${product.price}\nDescription: ${product.description}`);
            } else {
                logToTerminal(`Product with ID ${args[0]} not found.`);
            }
            break;
        case 'add':
            addToCart(parseInt(args[0]));
            break;
        case 'remove':
            removeFromCart(parseInt(args[0]));
            break;
        case 'cart':
            if (cart.length === 0) {
                logToTerminal('Your cart is empty.');
            } else {
                logToTerminal('Your cart contains:');
                cart.forEach(item => {
                    logToTerminal(`${item.id}: ${item.title} - $${item.price}`);
                });
            }
            break;
        case 'buy':
            if (cart.length > 0) {
                displayCheckoutPage();
            } else {
                logToTerminal('Your cart is empty. Add items before buying.');
            }
            break;
        case 'clear':
            terminalOutput.innerHTML = '';
            break;
        case 'help':
            logToTerminal(`Available commands:
- list: List all products.
- details [id]: Show details of a specific product.
- add [id]: Add a product to the cart.
- remove [id]: Remove a product from the cart.
- cart: View the contents of your cart.
- buy: Proceed to checkout.
- clear: Clear the terminal.
- help: Show available commands.`);
            break;
        default:
            logToTerminal('Unknown command. Type "help" to see available commands.');
    }
}

function displayCheckoutPage() {
    mainPage.style.display = 'none';
    checkoutPage.style.display = 'flex';
    displayCartItems();
}

function displayCartItems() {
    let totalAmount = 0;
    cartItemsContainer.innerHTML = '';

    cart.forEach(item => {
        totalAmount += item.price;

        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.title}">
            <div class="cart-item-details">
                <div class="cart-item-title">${item.title}</div>
                <div class="cart-item-price">$${item.price}</div>
            </div>
        `;
        cartItemsContainer.appendChild(cartItem);
    });
    

    const tax = totalAmount * 0.08;  // Assuming an 8% tax rate
    totalAmountElement.textContent = `$${(totalAmount + tax).toFixed(2)}`;
    totalTaxElement.textContent = `$${tax.toFixed(2)}`;
}

checkoutButton.addEventListener('click', () => {
    thankYouMessage.style.display = 'block';
    checkoutButton.style.display = 'none';
});

document.getElementById('commandInput').addEventListener('keydown', event => {
    if (event.key === 'Enter') {
        const command = event.target.value.trim();
        event.target.value = '';
        executeCommand(command);
    }
});

displayProducts();
