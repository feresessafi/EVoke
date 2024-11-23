<template>
  <aside
    class="w-64 border-r border-zinc-200 dark:border-zinc-800 bg-white dark:bg-zinc-900"
  >
    <div class="p-4 space-y-6">
      <!-- Logo -->
      <div class="flex items-center space-x-3 pb-2">
        <AppLogo />
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Home -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Overview
        </h3>
        <Button variant="ghost" class="w-full font-semibold justify-start">
          <LayoutDashboard class="mr-2 stroke-2" />
          Dashboard
        </Button>
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

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

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

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

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Settings -->
      <div class="space-y-1">
        <h3
          class="px-3 text-xs font-medium text-zinc-500 dark:text-zinc-400 uppercase tracking-wider"
        >
          Settings
        </h3>
        <Button
          v-for="item in settingsItems"
          :key="item.name"
          variant="ghost"
          class="w-full justify-start text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100"
        >
          <component :is="item.icon" class="mr-2 stroke-2" />
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
  Settings,
  LayoutDashboard,
} from "lucide-vue-next";

const IconNews = Newspaper;

const sourceItems = [
  { name: "Latest News", icon: Rss },
  { name: "Trending Topics", icon: ListFilter },
];

const articleItems = [
  { name: "Articles", icon: FileText }, // Single combined page
  { name: "Queue", icon: ListOrdered },
];

const settingsItems = [
  { name: "Account Settings", icon: Settings },
];
</script>
