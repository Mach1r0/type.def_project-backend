<template>
  <div class="container-header">
    <img
      src="../assets/logo_image.png"
      alt="Description of image"
      class="logo-style"
    />
    <router-link to="/home" class="title-page">TYPE.DEF</router-link>
  </div>
 <div class="container">
  <h1 class="title">REGISTER</h1>
  <div class="register">
        <input type="text" placeholder="Email adress" />
        <input type="text" placeholder="Username" />
        <input type="text" placeholder="Password" />
        <input type="text" placeholder="Confirm Password" />
        <button>REGISTER</button>
     <div class="text-under">
        <p>Alredy have an account?</p>
        <router-link to="/login" class="txt-login">Login</router-link>
    </div>
    <AppFooter class="signup-footer">
    </AppFooter>
</div>
  </div>
</template>

<script>
import AppFooter from './base/footer.vue'
export default {
  name: "SignUp",
  components:
  AppFooter
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Oswald:wght@200..700&display=swap");

/* Global styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Component-specific styles */
.container-header {
  display: flex;
  align-items: center;
}

.logo-style {
  max-width: 100px;
}

.title-page {
  font-style: none;
  text-decoration: none;
  font-size: 30px;
  font-weight: bold;
  color: black;
  padding: 0;
  margin-left: 30px;
  cursor: pointer;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 5vh; /* Adjust as needed */
}

.register {
  width: 50%;
  max-width: 420px;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 10px;
  margin: 0 auto;
  align-items: center;
}

.text-under {
  text-decoration: none;
  color: black;
}

.txt-login {
  color: black;
}

.register input {
  width: 100%;
  background-color: white;
}

.register button {
  width: 100%;
  background-color: rgb(0, 0, 0);
  cursor: pointer;
}

.register input,
button {
  height: 45px;
  border-radius: 7px;
  border: none;
  padding: 8px;
  outline: none;
  box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
}

.register input::placeholder {
  color: black;
}

.title {
  color: black;
  font-size: 30px;
  font-weight: bold;
  font-family: "inter", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
  text-align: center; /* Align center horizontally */
  margin-bottom: 20px; /* Add margin for better spacing */
}

.register button {
  color: white;
  border-radius: 10px;
  height: 50px;
  font-size: 15px;
  font-family: "Oswald", sans-serif;
}
</style>
