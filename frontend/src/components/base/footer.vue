<template>
   <footer class="signup-footer"> <!-- Add a specific class for SignUp footer -->
     <p> {{ footerText }} </p>
     <router-link to="/aboutus"> {{ aboutus }}</router-link >
     <router-link to="/privacy"> {{ Privacy }}</router-link >
     <router-link to="/instagram"> {{ Instagram }}</router-link >
   </footer>
 </template>
 
 <script>
 export default {
   name: 'AppFooter',
   data() {
     return {
       footerText: "Copyright 2003",
       aboutus: "About Us",
       Privacy: "Privacy",
       Instagram: "instagram",
     }
   }
 }
 </script>
 
 <style scoped>
 .signup-footer { 
   background: lightblue; 
   padding: 15px; 
   display: flex;
   align-items: center;
   justify-content: center;
   margin-top: 350px;
   justify-content: space-between;
 }
 </style>
 