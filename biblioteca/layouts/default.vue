<template>
  <div class="container">
    
        <TheHeader></TheHeader>

        <div id="conteinerMain">
            <slot />
        </div>
        
        <footer> <a href="https://github.com/SobrancelhaDoDragao" target="_blank">Desenvolvido por Eudson Durães © 2023</a><a href="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca" target="_blank">Github</a></footer>
        
        </div>

</template>


<style>
@import '~/assets/css/layoutDefault.css';
</style>