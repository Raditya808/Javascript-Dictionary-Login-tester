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
  },

{
  nama:'tiki',
  usergmail:'tikidih@gmail.com',
  userpassword:'tiki1234',
},
  {
    nama:'lulu',
    usergmail:'lulu@gmail.com',
    userpassword:'lulu123'
  }
]




// for form in tes_log
let user_gmail = document.getElementById('form-gmail');

let user_password = document.getElementById('form-password') 





// for log in document get element to form tes_log
function formlog(){

  
  if (user_gmail.value ==='' && user_password.value ===''){
    alert('Gmail / Password Tidak Boleh Kosong')
    
  }


  // dibungkus menggunakan for of didalam list dictionary 
  for (let i of data){
    if(user_gmail.value === i.usergmail && user_password.value === i.userpassword){
      window.location.href = `/dashboard` // dipanggil lewat route dari / flask  
      return
    }    
    
  }

  alert('Gmail/Password SALAH')

}





// data for sign up
const data_sec = [{}]


// dictionary sign up 
function sign_up(){
  for (let j of data){ // data dictionary sample data diatas untuk di bungkus


    let name = document.getElementById('nm')
    let gmail = document.getElementById('gm')
    let password = document.getElementById('pw')
    


    if(name.value ==='' && gmail.value ==='' && password.value ===''){
      alert('Kolom Ini Tidak Boleh Kosong!') 
    }else{

    // new sample data dic for signup elements
    let newdicuser = {
      nama:name.value,
      usergmail:gmail.value,
      userpassword:password.value
    }



    data_sec.push(newdicuser)
    
    alert('Pendaftaran Berhasil!')
    window.location.href = '/dashboard' // dipanggil lewat route menggunakan / dari flask
  }
  
    
  }

}


// cek data array apakah masuk di console 
console.log(data)
console.log(data_sec)







// to log out
let logout = document.getElementById('lg')
function log(){
  window.location.href = '/login' // dipanggil lewat route dari / flask 
}





