// html log make tipe data object melalui .value syntax untuk mengambil data 
//menggunakan button onClick


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

  
  // the condition if gmail and password is null
  if (user_gmail.value ==='' && user_password.value ===''){
    alert('Gmail / Password Tidak Boleh Kosong')
    return 
  }



  // the condition if gmail null 
  if (user_gmail.value ===''){
    alert('Gmail Tidak Boleh Kosong')
    return
  } 


  // the condition if password null
  if (user_password.value ===''){
      alert('Password Tidak Boleh Kosong')
    return
  }
  




  // dibungkus menggunakan for of didalam list dictionary 
  for (let i of data){
    if(user_gmail.value === i.usergmail && user_password.value === i.userpassword){
      //window.location.href = `/dashboard` // dipanggil lewat route dari / flask  
      //return
      if(i){
        // make sessionStorage.setItem for DOMContentLoaded form below
        // and take loop i from nama in object from data 
        with(i){
        sessionStorage.setItem('namauser',i.nama)
        

        // go to dashboard route using python flask
        window.location.href = '/dashboard'
        return
        }
      }
    }    
    
  }

  alert('Gmail/Password SALAH')

}





// DOM for formlog() 
// for take sessionStorage from formlog() and using sessionStorage.getitem
// using document.addEventListener and DOMContentLoaded and anonymouse function
document.addEventListener('DOMContentLoaded',function(){

  // take the id from result/success_form.html
  const html_id = document.getElementById('username_id')

  // take the sessionStorage.setItem from sessionStorage formlog() 
  const sessionname = sessionStorage.getItem('namauser')

  // use if condition using and (&&) and take the sessionname
  if(html_id && sessionname){
    
  // make it textContent so its show up from html 
    // and take the sessionname cause sessionname take the object from list + objects [{}]
    // using inner html to make html tag
   html_id.innerHTML = `
   
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Welcome</title>
      <link href="css/style.css" rel="stylesheet">
    </head>
  <body>
    <div class="card">
      <h3>${sessionname}</h3> 
    </div>
  </body>
</html>

  ` 
  }
   

})







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
      return 
    }else{

    // new sample data dic for signup elements
    let newdicuser = {
      nama:name.value,
      usergmail:gmail.value,
      userpassword:password.value
    } 


    // sucks if statement
    /*if (name.value ==='' && gmail.value){
      alert('Nama Tidak Boleh Kosong')
      return 
    }else if (gmail.value ===''){
      alert('Gmail Tidak Boleh Kosong')
      return 
    }else if (password.value ===''){
      alert('Password Tidak Boleh Kosong')
      return 
    } else if(name.value ===''&& gmail.value===''){
      alert('Nama / Gmail Tidak Boleh Kosong')
      return   
    }*/
    
    // nested list
    //data_sec.push(newdicuser)

    console.log(j.nama) 
    alert('Pendaftaran Berhasil!')
    window.location.href = '/dashboard' // dipanggil lewat route menggunakan / dari flask
  }
  
    
  }

}


// cek data array apakah masuk di console 
console.log(data)
console.log(data_sec)




// DOM for signup()



// to log out
let logout = document.getElementById('lg')
function log(){
  window.location.href = '/login' // dipanggil lewat route dari / flask 
}





