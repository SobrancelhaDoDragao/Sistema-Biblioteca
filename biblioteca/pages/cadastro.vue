<template>

    <div id="conteiner">

  
        <form action="">
            
            <h1>Cadastro</h1>

           <label for="nome">Nome</label>
           <input type="text" name="" id="nome">

           <label for="email">Email</label>
           <input type="email" name="" id="email">

           <label for="senha">Senha</label>
           <input type="password" name="" id="senha">

           <label for="senha">Repetir senha</label>
           <input type="password" name="" id="senha">

           <label for="tipoConta">Criar conta como</label>

            <select name="TipoConta" id="TipoConta">

                <option value="usuario">Usuário</option>
                <option value="funcionario">Funcionário</option>

            </select>


            <button>Cadastrar</button>

        </form>
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

#conteiner{
   height: 100vh;
   background: var(--colorOne);
   display: flex;
   justify-content: center;
   align-items: center; 
}

#conteiner form{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 50%;
}

form h1{
    color: var(--colorThree);
    font-weight: var(--bold-weight);
    font-size: 5rem;
    text-align: center;
    width: 100%;
    letter-spacing: 4px;
}


form > input{
    width: 100%;
    border:none;
    border-radius: 10px;
    padding: 10px;
    background:var(--main-background-color-conteiner);
    color: var(--colorFour);
    font-size: 1rem;
    outline: none;
    border: solid var(--colorSix) 1px;
}

form > label{
    color: var(--colorFour);
    margin: 10px 0 10px 0;
    width: 100%;
    font-size: 1.5rem;
    color: var(--main-background-color-conteiner);
}

form button{
    width: 50%;
    padding: 16px;
    margin: 25px;
    border: none;
    border-radius: 8px;
    display: block;
    outline: none;
    text-transform: uppercase;
    font-weight: var(--bold-weight);
    letter-spacing: 4px;
    color:var(--colorFour);
    background: var(--colorThree);
    cursor: pointer;
}

form select{
    width: 100%;
    border:none;
    border-radius: 5px;
    padding: 5px;
    background:var(--main-background-color-conteiner);
    color: var(--colorFour);
    font-size: 1rem;
    outline: none;
    border: solid var(--colorSix) 1px;
}

/* Mobile */
@media only screen and (max-width: 600px){
    #conteiner form{
        width: 90%;
    }

    form h1{
       font-size: 2.5rem;
    }


    form > label{
       font-size: 1rem;
    }

    form button{
        width: 100%;
    }
}
</style>

<script setup>
    useHead({
    title: 'Biblioteca | Cadastro',
    })
</script>