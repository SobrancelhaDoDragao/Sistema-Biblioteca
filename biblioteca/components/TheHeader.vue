<template>
     <header>
          
          <div class="logo">
                  <img src="~/assets/img/meninoLendo.png" alt=""> <span>Biblioteca</span>
          </div>

          <input type="checkbox" id="nav_check" hidden>

          <nav>
              <ul>
                  <li> <a href="#">Modo dark</a></li>
                  <li><NuxtLink to="home">Home</NuxtLink></li>
                  <li><NuxtLink to="acervo">Acervo</NuxtLink></li>
                  <li><NuxtLink to="user-information-page">{{ user.nome }}</NuxtLink></li>
              </ul>
          </nav>
          
          <label for="nav_check" class="hamburger" >
              <div></div>
              <div></div>
              <div></div>
          </label>

      </header>
</template>

<style scoped>
    header{
        /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/

        background: var(--main-background-color-conteiner);
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        padding: 0 40px;

        border-bottom: solid var(--colorOne) .5rem;
        
        background: var(--colorOne);
        background: linear-gradient(180deg, var(--colorOne) 50%, var(--colorFive) 90%);

    }

    nav ul{
        padding: 10px;
        background: var(--main-background-color-conteiner);
        border-radius: 10px;
        margin-top: .5rem;
    }

    .logo{
        margin-top: .5rem;
        display: flex;
        align-items: center;
    }

    .logo span{
        margin-left: .5rem;
        color:var(--colorThree);
        font-weight: var(--bold-weight);
        font-size: 1.5rem;
        letter-spacing: 2px;
    }

    nav ul{
        list-style: none;
        display: flex;
    }


    nav ul li a {
        text-decoration: none;
        display: block;
        color:var(--colorFour);
        margin: 0 2px;
        padding: 8px 18px;
        transition: 0.2s;
        border-radius: 30px;
    }

    nav ul li a:hover{
        background: var(--main-background-color);
    }

    .router-link-active, .router-link-exact-active{
        background: var(--colorOne);
        color:var(--colorThree);
        font-weight: var(--bold-weight);
    }
   
    .hamburger{
        display: none;
        height: fit-content;
        cursor: pointer;
        padding: 3px 8px;
        border-radius: 5px;
        transition: 0.2s;
        margin-top: 1rem;
    }

    .hamburger:hover{
        background: var(--main-background-color);
    }

    .hamburger div{
        width: 30px;
        height: 2px;
        margin: 6px 0;
        background: #212526;
    }

    .logo img{
        width: 60px;
        border-radius: 20px;
        border: solid var(--colorThree) 4px;
    }

    /* Reposividade do header */
  @media only screen and (max-width: 1100px){
      header{
         padding: 0 20px;
      }
  
      nav{
         position: absolute;
         left: -300px;
         top:0;
         z-index:999;
         width: 280px;
         height: 100vh;
         background-color:  #fefefe;
         transition: 0.2s;
         box-shadow: 2px 0 20px 0 rgba(0, 0, 0, 0.05);
      }
     
      #nav_check:checked ~ nav{
             left:0;
      }
  
      nav .logo {
         display: block;
         height: 70px;
         display: flex;
         align-items: center;
         margin-left: 30px;
      }
  
      nav ul li a{
         margin-bottom: 5px;
         padding: 10px 15px;
         border-radius: 5px;
      }
      nav ul{
        display: block;
        padding: 0 20px;
        margin-top: 30px;
      }
      
      .hamburger{
         display: block;
      }
  }
  
</style>


<script setup>
import { useUserStore } from '~/stores/user'

// Dados do usuário logado
const user = useUserStore()

// Só ira fazer o request se os dados do usuario estiver vazio
if(user.nome == ''){
    user.GetUserData()
}
</script>




