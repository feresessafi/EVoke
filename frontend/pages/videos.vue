<template>
  <div class="flex h-screen bg-zinc-50 dark:bg-zinc-950">
    <AppSidebar />

    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <div class="container mx-auto p-6 space-y-8 max-w-7xl">
        <!-- Header Section with improved styling -->
        <div class="flex justify-between items-center border-b dark:border-zinc-800 pb-6">
          <div>
            <h1 class="text-3xl font-bold text-zinc-900 dark:text-zinc-50 tracking-tight">
              Video Content
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400 mt-1">
              Latest video reviews and features
            </p>
          </div>
          <div class="flex items-center gap-3">
            <Select v-model="filterCategory">
              <SelectTrigger class="w-44 bg-white dark:bg-zinc-900">
                <SelectValue placeholder="All Categories" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Categories</SelectItem>
                <SelectItem value="reviews">Car Reviews</SelectItem>
                <SelectItem value="features">Feature Stories</SelectItem>
                <SelectItem value="news">News Updates</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- Featured Video Section with enhanced design -->
        <Card class="shadow-lg border-none bg-white/50 dark:bg-zinc-900/50 backdrop-blur-sm">
          <CardContent class="space-y-4 p-6">
            <!-- Video container with gradient border -->
            <div class="relative rounded-xl overflow-hidden bg-zinc-900 w-[70%] mx-auto mt-1 mb-3 ring-1 ring-zinc-200 dark:ring-zinc-800">
              <div class="absolute inset-0 bg-gradient-to-r from-primary/10 via-primary/5 to-transparent"></div>
              <video 
                class="w-full h-full object-contain"
                controls
                poster="/public/thumbnail.png"
              >
                <source src="/public/video.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
            </div>
            <!-- Enhanced video info section -->
            <div class="space-y-4 pt-2 px-4">
              <h3 class="text-2xl font-semibold leading-tight hover:text-primary transition-colors cursor-pointer">
                Porsche Announces High-Performance European Charging Network
              </h3>
              <p class="text-sm text-muted-foreground leading-relaxed max-w-3xl">
                Porsche has announced plans to develop its own high-performance charging network across Europe, featuring next-generation 450kW chargers. The network, dubbed 'Porsche TurboCharge,' will initially comprise 200 charging stations strategically located along major European highways.
              </p>
              <div class="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
                <Badge variant="secondary" class="bg-red-500/10 text-red-500 hover:bg-red-500/20">LIVE</Badge>
                <span class="flex items-center gap-1.5">
                  <Clock class="h-4 w-4" />
                  4:32
                </span>
                <span class="flex items-center gap-1.5">
                  <Calendar class="h-4 w-4" />
                  Nov 23, 2024
                </span>
                <Badge variant="secondary" class="bg-zinc-500/10">HD</Badge>
                <Badge variant="outline" class="text-xs">
                  Breaking News
                </Badge>
              </div>
              <div class="flex gap-3 text-xs text-muted-foreground pt-1 border-t dark:border-zinc-800">
                <a 
                  href="https://www.porsche.com/charging-network" 
                  target="_blank"
                  class="hover:text-primary transition-colors flex items-center gap-1"
                >
                  <Globe class="h-3 w-3" />
                  porsche.com
                </a>
                <span>•</span>
                <a 
                  href="https://www.electrive.com/porsche-turbocharge" 
                  target="_blank"
                  class="hover:text-primary transition-colors flex items-center gap-1"
                >
                  <ExternalLink class="h-3 w-3" />
                  electrive.com
                </a>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Video Grid with improved cards -->
        <div class="space-y-6">
          <div class="flex items-center justify-between">
            <h2 class="text-xl font-semibold tracking-tight">Recent Videos</h2>
            <Button variant="ghost" size="sm" class="text-muted-foreground">
              View All
              <ChevronRight class="h-4 w-4 ml-1" />
            </Button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            <Card 
              v-for="video in mockVideos" 
              :key="video.id"
              class="group hover:shadow-xl transition-all duration-300 bg-white/50 dark:bg-zinc-900/50 backdrop-blur-sm border-none"
            >
              <CardContent class="p-3">
                <!-- Enhanced thumbnail container -->
                <div class="relative aspect-video rounded-lg overflow-hidden mb-3 ring-1 ring-zinc-200 dark:ring-zinc-800">
                  <img 
                    :src="video.thumbnail" 
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                    alt="Video thumbnail"
                  />
                  <!-- Improved overlay with gradient -->
                  <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-black/0 group-hover:from-black/40 transition-colors duration-300" />
                  <div class="absolute inset-0 flex items-center justify-center opacity-90 group-hover:opacity-100 transition-all duration-300">
                    <div class="h-12 w-12 rounded-full bg-white/30 backdrop-blur-sm flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300 border border-white/30">
                      <Play class="h-6 w-6 text-white" fill="white" />
                    </div>
                  </div>
                  <Badge 
                    class="absolute top-2 right-2 bg-black/70 text-white backdrop-blur-sm"
                    variant="secondary"
                  >
                    {{ video.duration }}
                  </Badge>
                </div>
                <!-- Improved video info -->
                <div class="space-y-2 px-1">
                  <h3 class="font-medium text-sm leading-tight line-clamp-2 group-hover:text-primary transition-colors">
                    {{ video.title }}
                  </h3>
                  <div class="flex items-center justify-between text-xs text-muted-foreground">
                    <span class="flex items-center gap-1.5">
                      <Calendar class="h-3 w-3" />
                      {{ video.date }}
                    </span>
                    <span class="flex items-center gap-1.5">
                      <Eye class="h-3 w-3" />
                      {{ video.views }}
                    </span>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import AppSidebar from "@/components/AppSidebar.vue";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { Play, Clock, Calendar, Eye, Globe, ExternalLink, ChevronRight } from "lucide-vue-next";

const filterCategory = ref("all");

// Mock data for video grid
const mockVideos = [
  {
    id: 1,
    title: "BMW i4 M50 vs Tesla Model 3 Performance: Ultimate EV Showdown",
    thumbnail: "/thumbnails/bmw-tesla.jpg",
    duration: "12:45",
    date: "Feb 12, 2024",
    views: "24K views",
  },
  {
    id: 2,
    title: "Porsche Taycan Cross Turismo: Off-Road EV Adventure",
    thumbnail: "/thumbnails/porsche.jpg",
    duration: "18:20",
    date: "Feb 10, 2024",
    views: "18K views",
  },
  {
    id: 3,
    title: "Future of Electric Trucks: Rivian R1T Long-Term Review",
    thumbnail: "/thumbnails/rivian.jpg",
    duration: "21:15",
    date: "Feb 8, 2024",
    views: "32K views",
  },
  {
    id: 4,
    title: "Hyundai IONIQ 5 N: Game-Changing Performance EV",
    thumbnail: "/thumbnails/hyundai.jpg",
    duration: "15:30",
    date: "Feb 5, 2024",
    views: "28K views",
  },
  {
    id: 5,
    title: "Mercedes EQS SUV: Luxury Electric Family Transport",
    thumbnail: "/thumbnails/mercedes.jpg",
    duration: "19:45",
    date: "Feb 3, 2024",
    views: "21K views",
  },
  {
    id: 6,
    title: "Volkswagen ID. Buzz: Electric Van Revolution",
    thumbnail: "/thumbnails/vw.jpg",
    duration: "16:50",
    date: "Feb 1, 2024",
    views: "19K views",
  },
];
</script>

<style scoped>
.card-hover-effect {
  transition: transform 0.3s ease-in-out;
}

.card-hover-effect:hover {
  transform: translateY(-2px);
}
</style>
