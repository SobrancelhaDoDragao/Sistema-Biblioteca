<template>
    <div class="container">
      
     <TheHeader></TheHeader>

      <div id="conteinerMain">

          <TheSideBar></TheSideBar>

          <TheMain></TheMain>
          
      </div>
   
      <footer>Desenvolvido por Eudson Durães</footer>
      
    </div>
</template>

<style>

* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    font-family: var(--main-font);
    font-weight: var(--regular-weight);
}

body{
     background: var(--main-background-color);
}

.container{
    display: grid;
    height: 100vh;
    grid-template-columns: repeat(4,1fr);
    grid-template-rows: .3fr 1fr 1fr ;
    gap: 1rem;
}


#conteinerMain{
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
    grid-area: 2 / 1 / 4 / 5;
    display: flex;
    gap: 1rem;
    margin: 0 var(--margem-bordas) 0 var(--margem-bordas);
    flex-wrap: wrap;
}

footer{
    /*  grid-row-start | grid-column-start | grid-row-end | grid-column-end*/
    grid-area: 4 / 1 / 5 / 5;
    text-align: center;
    background-color: var(--colorOne);
    color: var(--main-background-color-conteiner);
}

/* Mobile */

@media only screen and (max-width:550px){
    .container{
        grid-template-columns: 1fr;
        grid-template-rows: .5fr 2fr 1fr .2fr;

    }

    main,#sidebar{
        margin:0;
    }
    main{
        flex: 2;
    }
    #sidebar{
        flex:1;
    }

    #conteinerMain{
        flex-direction: column;
        margin: 0 1rem 0 1rem;
        
    }

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