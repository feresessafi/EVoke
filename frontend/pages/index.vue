<template>
  <div class="flex h-screen bg-zinc-50 dark:bg-zinc-950">
    <AppSidebar />
    
    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <div class="p-6">
        <h1 class="text-2xl font-bold text-zinc-900 dark:text-zinc-50">Dashboard</h1>
        <!-- Add your dashboard content here -->
      </div>
    </main>
  </div>
</template>

<script setup>
import AppSidebar from '@/components/AppSidebar.vue';
</script>
