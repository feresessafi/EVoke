<template>
  <aside
    class="w-64 border-r border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900"
  >
    <div class="p-4 space-y-6">
      <div class="flex items-center space-x-3">
        <AppLogo />
      </div>

      <!-- Home -->
      <Button variant="ghost" class="w-full font-semibold justify-start">
        <Home class="mr-2 stroke-2" />
        Home
      </Button>

      <!-- Sources & Topics -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Sources
        </h3>
        <Button
          v-for="item in sourceItems"
          :key="item.name"
          variant="ghost"
          class="w-full justify-start text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100"
        >
          <component :is="item.icon" class="mr-2 h-4 w-4" />
          {{ item.name }}
        </Button>
      </div>

      <!-- Article Management -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Articles
        </h3>
        <Button
          v-for="item in articleItems"
          :key="item.name"
          variant="ghost"
          class="w-full justify-start text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100"
        >
          <component :is="item.icon" class="mr-2 h-4 w-4" />
          {{ item.name }}
        </Button>
      </div>

      <!-- Editor Tools -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Editor Tools
        </h3>
        <Button
          v-for="item in editorItems"
          :key="item.name"
          variant="ghost"
          class="w-full justify-start text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100"
        >
          <component :is="item.icon" class="mr-2 h-4 w-4" />
          {{ item.name }}
        </Button>
      </div>
    </div>
  </aside>
</template>

<script setup>
import { Button } from "@/components/ui/button";
import AppLogo from "@/components/AppLogo.vue";
import {
  Newspaper,
  Rss,
  FileText,
  PenSquare,
  Send,
  History,
  Lightbulb,
  MessagesSquare,
  ListFilter,
  BarChart2,
  Home,
  ListOrdered,
} from "lucide-vue-next";

const IconNews = Newspaper;

// News sources and topic management
const sourceItems = [
  { name: "Latest News", icon: Rss },
  { name: "Trending Topics", icon: ListFilter },
];

// Article workflow
const articleItems = [
  { name: "Drafts", icon: PenSquare },
  { name: "My Articles", icon: FileText },
  { name: "Queue", icon: ListOrdered },
  { name: "Published", icon: Send },
  
];

// AI assistance tools for editors
const editorItems = [
  { name: "Performance", icon: BarChart2 },
  { name: "Article History", icon: History },
  { name: "Feedback", icon: MessagesSquare },
];
</script>
