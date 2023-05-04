<template>
      <div class="container">
        <NuxtLoadingBar/>
        <TheHeader></TheHeader>
        <div id="conteinerMain">
            <slot />
        </div>
        
        <footer> <a href="https://github.com/SobrancelhaDoDragao" target="_blank">Desenvolvido por Eudson Durães © 2023</a><a href="https://github.com/SobrancelhaDoDragao/Sistema-Biblioteca" target="_blank" class="FooterLinkOculto" >Github</a> <a href="https://www.linkedin.com/in/eudsonduraes/" target="_blank" class="FooterLinkOculto" >Linkedin</a></footer>
        
      </div>

</template>


<style>
@import '~/assets/css/layoutDefault.css';
</style>