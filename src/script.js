// html log make tipe data object melalui .value syntax untuk mengambil data 
// menggunakan button onClick


// dictionary list 
// sample data
const data = [

{
  nama:'Muhammad Raditya Ramadhan',
  usergmail:'radit@gmail.com',
  userpassword:'12345',
},
  
{
  nama:'Lmao',
  usergmail:'lmao@gmail.com',
  userpassword:'54321',
},
{
  nama:'dita',
  usergmail:'dita@gmail.com',
  userpassword:'dita123',
},

  {
    nama:'kiki',
    usergmail:'kiki@gmail.com',
    userpassword:'kiki123'
  }
]


// for form in tes_log
let user_input = document.getElementById('form-input');

let user_password = document.getElementById('form-password') 


// for log in document get element to form tes_log
function formlog(){
  
  if (user_input.value ==='' && user_password.value ===''){
    alert('Gmail / Password Tidak Boleh Kosong')
    
  }else{
    alert('Gmail / Password Salah')
  }

  // dibungkus menggunakan for of didalam list dictionary 
  for (let i of data){
    if(user_input.value === i.usergmail && user_password.value === i.userpassword){
      window.location.href = 'success_form.html'  
      return
    }
    
  }

}


// send to form after login the username 
// next feature
