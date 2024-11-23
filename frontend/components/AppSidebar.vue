<template>
  <aside
    class="w-64 border-r border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900"
  >
    <div class="p-4 space-y-6">
      <!-- Logo -->
      <div class="flex items-center space-x-3 pb-2 pt-4">
        <AppLogo />
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Main Navigation -->
      <div class="space-y-1">
        <NuxtLink to="/">
          <Button variant="ghost" class="w-full justify-start font-semibold">
            <LayoutDashboard class="mr-2 h-4 w-4" />
            Dashboard
          </Button>
        </NuxtLink>
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Content Generation -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Generation
        </h3>
        <NuxtLink to="/review">
          <Button variant="ghost" class="w-full justify-start relative">
            <ListStart class="mr-2 h-4 w-4" />
            Review Queue
            <Badge variant="secondary" class="ml-auto">{{ reviewCount }}</Badge>
          </Button>
        </NuxtLink>
        <Button variant="ghost" class="w-full justify-start" @click="(e) => showComingSoon('News Feed', e)">
          <Newspaper class="mr-2 h-4 w-4" />
          News Feed
        </Button>
        <Button variant="ghost" class="w-full justify-start" @click="(e) => showComingSoon('Article Generation', e)">
          <PlusCircle class="mr-2 h-4 w-4" />
          Generate Article
        </Button>
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Content Management -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Content
        </h3>
        
        <NuxtLink to="/published">
          <Button variant="ghost" class="w-full justify-start">
            <CheckCheck class="mr-2 h-4 w-4" />
            Published
          </Button>
        </NuxtLink>
        <NuxtLink to="/videos">
          <Button variant="ghost" class="w-full justify-start">
            <Camera class="mr-2 h-4 w-4" />
            Videos
          </Button>
        </NuxtLink>
        <NuxtLink to="/podcasts">
          <Button variant="ghost" class="w-full justify-start">
            <Mic class="mr-2 h-4 w-4" />
            Podcasts
          </Button>
        </NuxtLink>
        <NuxtLink to="/archive">
          <Button variant="ghost" class="w-full justify-start">
            <Archive class="mr-2 h-4 w-4" />
            Archive
          </Button>
        </NuxtLink>
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Settings & Help -->
      <div class="space-y-1">
        <Button variant="ghost" class="w-full justify-start" @click="(e) => showComingSoon('Settings', e)">
          <Settings class="mr-2 h-4 w-4" />
          Settings
        </Button>
        <Button variant="ghost" class="w-full justify-start" @click="(e) => showComingSoon('Help Center', e)">
          <HelpCircle class="mr-2 h-4 w-4" />
          Help
        </Button>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  LayoutDashboard,
  Rss,
  Wand2,
  PenSquare,
  CheckSquare,
  Archive,
  Settings,
  HelpCircle, 
  Newspaper,
  PlusCircle, 
  BookCheck,
  ListStart,
  CheckCheck,
  Camera, 
  Mic,
} from "lucide-vue-next";
import AppLogo from "./AppLogo.vue";
import { useToast } from '@/components/ui/toast/use-toast';

// These would come from your store in real app

const store = useStore();
const { reviewNeededArticles } = storeToRefs(store);
//const draftCount = 3;
const reviewCount = reviewNeededArticles.value.length;

const { toast } = useToast();

const showComingSoon = (feature: string, event: Event) => {
  // Add shake animation to the clicked button
  const button = event.currentTarget as HTMLElement;
  button.classList.add('shake');
  
  // Remove the shake class after animation completes
  setTimeout(() => {
    button.classList.remove('shake');
  }, 300);

  toast({
    title: `${feature} Coming Soon`,
    description: `We're working hard to bring you ${feature.toLowerCase()}. Stay tuned!`,
  });
};
</script>
