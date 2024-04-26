let select = document.getElementById("Thickness");

for (let i = 1; i <= 20; i++) {
  let option = document.createElement("option");
  option.text = i;
  option.value = i;
  select.appendChild(option);
}


let selectwidth = document.getElementById("Width");

for (let i = 500; i <= 2000; i++) {
  let option = document.createElement("option");
  option.text = i;
  option.value = i;
  selectwidth.appendChild(option);
}



const selector = document.querySelector('.custom-selector');

selector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


const selector1 = document.querySelector('.custom-selector1');

selector1.addEventListener('change',e => {
    console.log('changed',e.target.value);
})




const customerselector = document.querySelector('.custom_customer');

customerselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


const Productselector = document.querySelector('.custom_Product');

Productselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})



const Materialselector = document.querySelector('.custom_Material');

Productselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})




const Applicationselector = document.querySelector('.custom_Application');

Applicationselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})



const Itemtypeselector = document.querySelector('.custom_Itemtype');

Itemtypeselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})




const countryselector = document.querySelector('.custom_country');

countryselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


