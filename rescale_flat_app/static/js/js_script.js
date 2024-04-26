let select = document.getElementById("Floor_Area");

for (let i = 38; i <= 156; i++) {
  let option = document.createElement("option");
  option.text = i;
  option.value = i;
  select.appendChild(option);
}




const Min_Storeyselector = document.querySelector('.custom-Min_Storey');

Min_Storeyselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


const Max_Storeyselector = document.querySelector('.custom-Max_Storey');

Max_Storeyselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


const selectorYear = document.querySelector('.custom-Year');

selectorYear.addEventListener('change',e => {
    console.log('changed',e.target.value);
})





const Leaseselector = document.querySelector('.custom_Lease_Year');

Leaseselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})




const Flatselector = document.querySelector('.custom_Flat_type');

Flatselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})




const FloorAreaselector = document.querySelector('.custom_Floor_Area');

FloorAreaselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})


const Modelselector = document.querySelector('.custom_Flat_Model');

Modelselector.addEventListener('change',e => {
    console.log('changed',e.target.value);
})