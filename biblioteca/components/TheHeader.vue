<template>
     <header>
          
          <div class="logo">
                  <nuxt-img src="img/meninoLendo.png" format="webp" width="60" height="60"/><span>Biblioteca</span>
          </div>

          <input type="checkbox" id="nav_check" hidden>

          <nav>
              <ul>
              
                  <li><NuxtLink to="/auth/home">Home</NuxtLink></li>
                  <li><NuxtLink to="/auth/acervo/livros">Acervo</NuxtLink></li>
                  <li><NuxtLink to="/auth/gerenciar-emprestimos/emprestimos">Empréstimos</NuxtLink></li>
                  <li><NuxtLink to="/auth/user-information-page" id="UserNomeEFoto">

                    <nuxt-img  v-if="user.foto == null" src="icons/user-solid.svg" format="webp" width="20" height="20"/>
                    <nuxt-img  v-else :src="user.foto" format="webp" width="20" height="15"/>
                    {{ user.nome }}
                    </NuxtLink>
                    
                  </li>

                  <label for="nav_check" class="hamburger fecharNavBar" >
                    <h1>X</h1>
                  </label>
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
        background: linear-gradient(180deg, var(--colorOne) 50%, var(--colorFour) 90%);

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
        color:var(--colorTwo);
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
        color:var(--colorThree);
        margin: 0 5px;
        padding: 10px;
        transition: 0.2s;
        border-radius: 10px;
        border-bottom: solid 5px var(--colorFive);
        border-right:solid 2px var(--colorFive);
    }

    nav ul li a:hover{
        background: var(--main-background-color);
    }

    .router-link-active, .router-link-exact-active{
        background: var(--colorOne);
        color:var(--colorTwo);
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
        border-radius: 20px;
        border: solid var(--colorTwo) 4px;
    }

    #UserNomeEFoto{
        display: flex;
        gap: 5px;
        align-items: center;
    }

    .fecharNavBar{
        border: solid var(--colorFive);
    }

    /* Reposividade do header */
  @media only screen and (max-width: 1100px){
      header{
         padding: 0 20px;
      }
  
      nav{
         position: absolute;
         left: -50vw;
         top:0;
         z-index:999;
         width: 50vw;
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

  @media only screen and (max-width:  600px){
 
      nav{
         left: -85vw;
         width: 85vw;
      }
   

     
  }
  
</style>


<script setup>

// Dados do usuário logado
let user = useUserStore()

// Só ira fazer o request se os dados do usuario estiver vazio
if(user.nome == ''){
    await user.GetUserData()
}
</script>




