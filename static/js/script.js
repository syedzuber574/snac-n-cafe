// ---------------------------
// LOAD CART
// ---------------------------

let cart =
    JSON.parse(localStorage.getItem("cart"))
    || [];


// ---------------------------
// SAVE CART
// ---------------------------

function saveCart() {

    localStorage.setItem(
        "cart",
        JSON.stringify(cart)
    );
}


// ---------------------------
// UPDATE CART COUNT
// ---------------------------

function updateCartCount() {

    let countElement =
        document.getElementById(
            "cart-count"
        );

    if (!countElement) return;

    let totalItems = 0;

    cart.forEach(item => {

        totalItems += item.quantity;
    });

    countElement.innerText =
        totalItems;
}


// ---------------------------
// ADD TO CART
// ---------------------------

function addToCart(button) {

    let card =
        button.closest(".food-card");

    let itemName =
        card.querySelector("h3").innerText;

    let itemPrice =
        parseInt(
            card.querySelector(".price-value")
            .innerText
        );

    let itemImage =
        card.querySelector("img").src;

    let existingItem =
        cart.find(item =>
            item.name === itemName
        );

    if (existingItem) {

        existingItem.quantity++;

    } else {

        cart.push({
            name: itemName,
            price: itemPrice,
            image: itemImage,
            quantity: 1
        });
    }

    saveCart();

    updateBurgerPage();
    updateCartPage();
    updateCartCount();
}


// ---------------------------
// INCREASE
// ---------------------------

function increase(button) {

    let card =
        button.closest(".food-card");

    let itemName =
        card.querySelector("h3").innerText;

    let item =
        cart.find(i =>
            i.name === itemName
        );

    if (item) {

        item.quantity++;

        saveCart();

        updateBurgerPage();
        updateCartPage();
        updateCartCount();
    }
}


// ---------------------------
// DECREASE
// ---------------------------

function decrease(button) {

    let card =
        button.closest(".food-card");

    let itemName =
        card.querySelector("h3").innerText;

    let item =
        cart.find(i =>
            i.name === itemName
        );

    if (!item) return;

    item.quantity--;

    if (item.quantity <= 0) {

        cart =
            cart.filter(i =>
                i.name !== itemName
            );
    }

    saveCart();

    updateBurgerPage();
    updateCartPage();
    updateCartCount();
}


// ---------------------------
// REMOVE ITEM
// ---------------------------

function removeItem(itemName) {

    cart =
        cart.filter(item =>
            item.name !== itemName
        );

    saveCart();

    updateBurgerPage();
    updateCartPage();
    updateCartCount();
}


// ---------------------------
// CLEAR CART
// ---------------------------

function clearCart() {

    cart = [];

    saveCart();

    updateBurgerPage();
    updateCartPage();
    updateCartCount();
}


// ---------------------------
// UPDATE FOOD PAGE
// ---------------------------

function updateBurgerPage() {

    let cards =
        document.querySelectorAll(
            ".food-card"
        );

    cards.forEach(card => {

        let h3 =
            card.querySelector("h3");

        if (!h3) return;

        let itemName =
            h3.innerText;

        let item =
            cart.find(i =>
                i.name === itemName
            );

        let addButton =
            card.querySelector(".cart-btn");

        let quantityBox =
            card.querySelector(".quantity-box");

        let quantityText =
            card.querySelector(".quantity");

        if (
            !addButton ||
            !quantityBox ||
            !quantityText
        ) return;

        if (item) {

            addButton.style.display =
                "none";

            quantityBox.style.display =
                "flex";

            quantityText.innerText =
                item.quantity;

        } else {

            addButton.style.display =
                "inline-block";

            quantityBox.style.display =
                "none";
        }
    });
}


// ---------------------------
// UPDATE CART PAGE
// ---------------------------

function updateCartPage() {

    let cartItems =
        document.getElementById(
            "cart-items"
        );

    let totalPrice =
        document.getElementById(
            "total-price"
        );

    if (!cartItems) return;

    cartItems.innerHTML = "";

    let total = 0;

    cart.forEach(item => {

        total +=
            item.price * item.quantity;

        cartItems.innerHTML += `

        <div class="food-card">

            <img src="${item.image}">

            <h3>${item.name}</h3>

            <p>₹${item.price}</p>

            <div class="quantity-box">

                <button onclick="decrease(this)">
                    −
                </button>

                <span class="quantity">
                    ${item.quantity}
                </span>

                <button onclick="increase(this)">
                    +
                </button>

            </div>

            <button
            onclick="removeItem('${item.name}')">
                🗑️ Remove
            </button>

        </div>
        `;
    });

    totalPrice.innerText =
        "Total: ₹" + total;
}


// ---------------------------
// SMART SEARCH SYSTEM
// ---------------------------

function setupSearch() {

    let searchInput =
        document.getElementById(
            "foodSearch"
        );

    let suggestionsBox =
        document.getElementById(
            "searchSuggestions"
        );

    if (
        !searchInput ||
        !suggestionsBox
    ) return;

    const foods = {

        "burger": "/burger",
        "veg burger": "/burger",
        "aloo tikki burger": "/burger",
        "chicken burger": "/burger",

        "pizza": "/pizza",
        "veg pizza": "/pizza",
        "chicken pizza": "/pizza",

        "momos": "/momos",
        "veg momos": "/momos",

        "fries": "/fries",
        "french fries": "/fries",

        "falooda": "/falooda",
        "mojito": "/mojito",
        "lemonade": "/lemonade",
        "smoothie": "/smoothie",

        "rolls": "/rolls",
        "shawarma roll": "/rolls",

        "sandwich": "/sandwiches",
        "sandwiches": "/sandwiches",

        "oreo milkshake": "/milk_shakes",
        "milkshake": "/milk_shakes",

        "fresh juice": "/fresh_juices",
        "juice": "/fresh_juices",

        "fried chicken": "/fried_chicken",
        "combo": "/combo"
    };


    function getHistory() {

        return JSON.parse(
            localStorage.getItem(
                "searchHistory"
            )
        ) || [];
    }


    function saveHistory(search) {

        let history =
            getHistory();

        history =
            history.filter(
                item => item !== search
            );

        history.unshift(search);

        history =
            history.slice(0, 10);

        localStorage.setItem(
            "searchHistory",
            JSON.stringify(history)
        );
    }


    function showSuggestions(
        items,
        historyMode = false
    ) {

        suggestionsBox.innerHTML =
            "";

        if (
            historyMode &&
            items.length > 0
        ) {

            suggestionsBox.innerHTML += `
            <div class="suggestion-item"
            style="
            font-weight:bold;
            background:#fff4d6;">
                Recent Searches

                <button
                class="clear-history-btn"
                onclick="clearSearchHistory()">
                    Clear
                </button>
            </div>
            `;
        }

        items.forEach(food => {

            suggestionsBox.innerHTML += `
            <div class="suggestion-item">

                <span
                onclick="goToFood('${food}')"
                style="
                flex:1;
                cursor:pointer;">
                    ${food}
                </span>

                ${historyMode
                ?
                `<button
                onclick="removeHistory('${food}')"
                style="
                border:none;
                background:none;
                cursor:pointer;
                font-size:18px;">
                    ❌
                </button>`
                :
                ""
                }

            </div>
            `;
        });

        suggestionsBox.style.display =
            items.length > 0
            ? "block"
            : "none";
    }


    window.goToFood =
    function(food) {

        saveHistory(food);

        window.location.href =
            foods[food];
    };


    window.removeHistory =
    function(food) {

        let history =
            getHistory();

        history =
            history.filter(
                item => item !== food
            );

        localStorage.setItem(
            "searchHistory",
            JSON.stringify(history)
        );

        showSuggestions(
            history,
            true
        );
    };


    window.clearSearchHistory =
    function() {

        localStorage.removeItem(
            "searchHistory"
        );

        suggestionsBox.innerHTML =
            "";

        suggestionsBox.style.display =
            "none";
    };


    searchInput.addEventListener(
        "focus",
        function() {

            let history =
                getHistory();

            showSuggestions(
                history,
                true
            );
        }
    );


    searchInput.addEventListener(
        "input",
        function() {

            let search =
                searchInput.value
                .toLowerCase()
                .trim();

            if (search === "") {

                showSuggestions(
                    getHistory(),
                    true
                );

                return;
            }

            let matches =
                Object.keys(foods)
                .filter(food =>
                    food.includes(search)
                );

            showSuggestions(matches);
        }
    );


    searchInput.addEventListener(
        "keypress",
        function(event) {

            if (
                event.key !== "Enter"
            ) return;

            let search =
                searchInput.value
                .toLowerCase()
                .trim();

            let matchedFood =
                Object.keys(foods)
                .find(food =>
                    food.includes(search)
                );

            if (matchedFood) {

                saveHistory(
                    matchedFood
                );

                window.location.href =
                    foods[matchedFood];

            } else {

                alert(
                    "Food not found"
                );
            }
        }
    );
}


// ---------------------------
// SEND WHATSAPP ORDER
// ---------------------------

function sendWhatsAppOrder() {

    let customerName =
        document.getElementById(
            "customer-name"
        ).value;

    let customerPhone =
        document.getElementById(
            "customer-phone"
        ).value;

    let customerAddress =
        document.getElementById(
            "customer-address"
        ).value;

    if (
        customerName === "" ||
        customerPhone === "" ||
        customerAddress === ""
    ) {

        alert(
            "Please fill all details"
        );

        return;
    }

    let total = 0;

    let itemsText = "";

    let orderMessage =
`🍔 Snac N Cafe Order

Name: ${customerName}
Phone: ${customerPhone}
Address: ${customerAddress}

Items:
`;

    cart.forEach(item => {

        total +=
            item.price *
            item.quantity;

        itemsText +=
`${item.name}
Qty: ${item.quantity}
Price: ₹${item.price}

`;

        orderMessage +=
`${item.name}
Qty: ${item.quantity}
Price: ₹${item.price}

`;
    });

    let orderId =
        "SNC" +
        Math.floor(
            Math.random() * 100000
        );

    orderMessage +=
`Order ID: ${orderId}

Total: ₹${total}`;

    fetch(
        "/save-order",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/x-www-form-urlencoded"
            },

            body:
                "customer_name=" +
                encodeURIComponent(customerName) +

                "&phone=" +
                encodeURIComponent(customerPhone) +

                "&address=" +
                encodeURIComponent(customerAddress) +

                "&items=" +
                encodeURIComponent(itemsText) +

                "&total=" +
                encodeURIComponent(total)
        }
    )

    .then(
        response =>
        response.text()
    )

    .then(data => {

        let whatsappNumber =
            "918310426661";

        let whatsappURL =
`https://wa.me/${whatsappNumber}?text=${encodeURIComponent(orderMessage)}`;

        window.open(
            whatsappURL,
            "_blank"
        );

        cart = [];

        saveCart();

        updateCartPage();
        updateBurgerPage();
        updateCartCount();
    })

    .catch(error => {

        console.log(error);

        alert(
            "Order save failed"
        );
    });
}


// ---------------------------
// PAGE LOAD
// ---------------------------

window.onload = function () {

    updateBurgerPage();
    updateCartPage();
    updateCartCount();
    setupSearch();
};