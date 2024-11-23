<template>
  <div class="p-8 space-y-4">
    <h1 class="text-3xl text-red-700 font-bold underline">
      Hello world!
    </h1>
    
    <div class="space-y-2">
      <p class="text-lg">Count: {{ counter.count }}</p>
      <p class="text-lg">Double Count: {{ counter.doubleCount }}</p>
      
      <div class="space-x-2">
        <Button @click="counter.increment()">Increment</Button>
        <Button variant="outline" @click="counter.decrement()">Decrement</Button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '~/stores/store'

const counter = useCounterStore()
</script>