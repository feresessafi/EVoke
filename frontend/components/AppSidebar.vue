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
        <Button variant="ghost" class="w-full justify-start font-semibold">
          <LayoutDashboard class="mr-2 h-4 w-4" />
          Dashboard
        </Button>
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
        <Button variant="ghost" class="w-full justify-start">
          <Rss class="mr-2 h-4 w-4" />
          News Feed
        </Button>
        <Button variant="ghost" class="w-full justify-start">
          <Wand2 class="mr-2 h-4 w-4" />
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
        <Button variant="ghost" class="w-full justify-start relative">
          <PenSquare class="mr-2 h-4 w-4" />
          Drafts
          <Badge variant="secondary" class="ml-auto">{{ draftCount }}</Badge>
        </Button>
        <Button variant="ghost" class="w-full justify-start relative">
          <CheckSquare class="mr-2 h-4 w-4" />
          Review Queue
          <Badge variant="primary" class="ml-auto">{{ reviewCount }}</Badge>
        </Button>
        <Button variant="ghost" class="w-full justify-start">
          <Archive class="mr-2 h-4 w-4" />
          Published
        </Button>
      </div>

      <!-- Thin Divider -->
      <div class="border-t border-zinc-200 dark:border-zinc-800 my-2" />

      <!-- Settings & Help -->
      <div class="space-y-1">
        <Button variant="ghost" class="w-full justify-start">
          <Settings class="mr-2 h-4 w-4" />
          Settings
        </Button>
        <Button variant="ghost" class="w-full justify-start">
          <HelpCircle class="mr-2 h-4 w-4" />
          Help
        </Button>
      </div>
    </div>
  </aside>
</template>

<script setup>
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
} from "lucide-vue-next";
import AppLogo from "./AppLogo.vue";

// These would come from your store in real app
const draftCount = 3;
const reviewCount = 8;
</script>
