<template>
  <div class="flex h-screen bg-zinc-50 dark:bg-zinc-950">
    <AppSidebar />

    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <div class="container mx-auto p-6 space-y-8 max-w-7xl">
        <!-- Header Section -->
        <div class="flex justify-between items-center border-b dark:border-zinc-800 pb-6">
          <div>
            <h1 class="text-3xl font-bold text-zinc-900 dark:text-zinc-50 tracking-tight">
              EV Podcast
            </h1>
            <p class="text-sm text-zinc-500 dark:text-zinc-400 mt-1">
              In-depth discussions about electric vehicles and sustainable mobility
            </p>
          </div>
          <div class="flex items-center gap-3">
            <Select v-model="filterCategory">
              <SelectTrigger class="w-44 bg-white dark:bg-zinc-900">
                <SelectValue placeholder="All Episodes" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="all">All Episodes</SelectItem>
                <SelectItem value="interviews">Interviews</SelectItem>
                <SelectItem value="reviews">Car Reviews</SelectItem>
                <SelectItem value="news">Industry News</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>

        <!-- Latest Episode Section -->
        <Card class="shadow-lg border-none bg-white/50 dark:bg-zinc-900/50 backdrop-blur-sm">
          <CardContent class="p-6">
            <div class="flex flex-col lg:flex-row gap-6">
              <!-- Podcast Player -->
              <div class="lg:w-1/3">
                <div class="aspect-square rounded-xl overflow-hidden ring-1 ring-zinc-200 dark:ring-zinc-800 relative group">
                  <img 
                    src="/public/nicecar.jpeg" 
                    alt="Latest episode cover"
                    class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
                  />
                  <div class="absolute inset-0 bg-black/30 group-hover:bg-black/20 transition-colors flex items-center justify-center">
                    <div class="h-16 w-16 rounded-full bg-white/20 backdrop-blur-sm flex items-center justify-center transform group-hover:scale-110 transition-transform duration-300 border border-white/30">
                      <Play class="h-8 w-8 text-white" fill="white" />
                    </div>
                  </div>
                </div>
                <!-- Audio Player -->
                <div class="mt-4 space-y-4">
                  <div class="w-full bg-zinc-200 dark:bg-zinc-800 rounded-full h-1">
                    <div 
                      class="bg-primary h-1 rounded-full transition-all duration-300"
                      :style="{ width: `${progress}%` }"
                    ></div>
                  </div>
                  <div class="flex items-center justify-between text-sm text-muted-foreground">
                    <span>{{ currentTime }}</span>
                    <span>{{ duration }}</span>
                  </div>
                  <div class="flex items-center justify-center gap-4">
                    <Button variant="ghost" size="icon" @click="skipBackward">
                      <SkipBack class="h-6 w-6" />
                    </Button>
                    <Button 
                      size="icon" 
                      class="h-12 w-12 rounded-full"
                      @click="togglePlay"
                    >
                      <component 
                        :is="isPlaying ? Pause : Play" 
                        class="h-6 w-6"
                      />
                    </Button>
                    <Button variant="ghost" size="icon" @click="skipForward">
                      <SkipForward class="h-6 w-6" />
                    </Button>
                  </div>
                </div>
              </div>

              <!-- Episode Info -->
              <div class="lg:w-2/3 space-y-4">
                <Badge variant="secondary" class="bg-primary/10 text-primary">Latest Episode</Badge>
                <h2 class="text-2xl font-semibold">The Future of EV Charging Infrastructure</h2>
                <p class="text-sm text-muted-foreground leading-relaxed">
                  In this episode, we dive deep into Porsche's ambitious plans for a high-performance charging network across Europe. 
                  We discuss the technical challenges, the impact on EV adoption, and what this means for the future of electric mobility. 
                  This episode is a must-listen for anyone interested in the future of electric vehicles and sustainable mobility.

                </p>
                <div class="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
                  <span class="flex items-center gap-1.5">
                    <Calendar class="h-4 w-4" />
                    Feb 15, 2024
                  </span>
                  <span class="flex items-center gap-1.5">
                    <Clock class="h-4 w-4" />
                    45:30
                  </span>
                  <span class="flex items-center gap-1.5">
                    <Headphones class="h-4 w-4" />
                    12K listens
                  </span>
                </div>
                <div class="flex gap-3 pt-4 border-t dark:border-zinc-800">
                  <Button variant="outline" class="gap-2">
                    <Share2 class="h-4 w-4" />
                    Share
                  </Button>
                  <Button variant="outline" class="gap-2">
                    <Download class="h-4 w-4" />
                    Download
                  </Button>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>

        <!-- Previous Episodes -->
        <div class="space-y-6">
          <div class="flex items-center justify-between">
            <h2 class="text-xl font-semibold tracking-tight">Previous Episodes</h2>
            <Button variant="ghost" size="sm" class="text-muted-foreground">
              View All Episodes
              <ChevronRight class="h-4 w-4 ml-1" />
            </Button>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Card 
              v-for="episode in previousEpisodes" 
              :key="episode.id"
              class="group hover:shadow-xl transition-all duration-300 bg-white/50 dark:bg-zinc-900/50 backdrop-blur-sm border-none"
            >
              <CardContent class="p-4">
                <div class="flex gap-4">
                  <div class="relative w-24 h-24 rounded-lg overflow-hidden ring-1 ring-zinc-200 dark:ring-zinc-800">
                    <img 
                      :src="episode.cover" 
                      :alt="episode.title"
                      class="w-full h-full object-cover"
                    />
                  </div>
                  <div class="flex-1 min-w-0 space-y-2">
                    <h3 class="font-medium text-sm leading-tight line-clamp-2 group-hover:text-primary transition-colors">
                      {{ episode.title }}
                    </h3>
                    <div class="flex flex-col gap-1 text-xs text-muted-foreground">
                      <span class="flex items-center gap-1">
                        <Calendar class="h-3 w-3" />
                        {{ episode.date }}
                      </span>
                      <span class="flex items-center gap-1">
                        <Clock class="h-3 w-3" />
                        {{ episode.duration }}
                      </span>
                    </div>
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
import { ref, onMounted, onUnmounted } from 'vue';
import AppSidebar from '@/components/AppSidebar.vue';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent } from '@/components/ui/card';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { 
  Play, 
  SkipBack,
  SkipForward,
  Clock, 
  Calendar,
  Headphones,
  Share2,
  Download,
  ChevronRight,
  Pause,
} from 'lucide-vue-next';

const filterCategory = ref('all');

// Mock data for previous episodes
const previousEpisodes = [
  {
    id: 1,
    title: "Interview: BMW's Chief EV Designer on Future Design Language",
    cover: "/bmw.jpeg",
    date: "Feb 10, 2024",
    duration: "38:45",
  },
  {
    id: 2,
    title: "Deep Dive: Solid State Batteries Explained",
    cover: "/ev-battery.jpeg",
    date: "Feb 5, 2024",
    duration: "42:15",
  },
  {
    id: 3,
    title: "Tesla Model 3 Highland: Comprehensive Review",
    cover: "/teslamodel3.jpeg",
    date: "Jan 30, 2024",
    duration: "35:20",
  },
];

// Audio player state
const audio = ref<HTMLAudioElement | null>(null);
const isPlaying = ref(false);
const currentTime = ref('00:00');
const duration = ref('45:30');
const progress = ref(0);

// Initialize audio
onMounted(() => {
  audio.value = new Audio("/public/Porsche.mp3");
  
  // Add event listeners
  audio.value.addEventListener('timeupdate', updateProgress);
  audio.value.addEventListener('ended', handleEnded);
  audio.value.addEventListener('loadedmetadata', updateDuration);
});

// Cleanup
onUnmounted(() => {
  if (audio.value) {
    audio.value.removeEventListener('timeupdate', updateProgress);
    audio.value.removeEventListener('ended', handleEnded);
    audio.value.removeEventListener('loadedmetadata', updateDuration);
    audio.value.pause();
  }
});

// Audio control functions
const togglePlay = () => {
  if (!audio.value) return;
  
  if (isPlaying.value) {
    audio.value.pause();
  } else {
    audio.value.play();
  }
  isPlaying.value = !isPlaying.value;
};

const skipBackward = () => {
  if (!audio.value) return;
  audio.value.currentTime = Math.max(0, audio.value.currentTime - 10);
};

const skipForward = () => {
  if (!audio.value) return;
  audio.value.currentTime = Math.min(audio.value.duration, audio.value.currentTime + 10);
};

// Helper functions
const formatTime = (seconds: number): string => {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);
  return `${minutes.toString().padStart(2, '0')}:${remainingSeconds.toString().padStart(2, '0')}`;
};

const updateProgress = () => {
  if (!audio.value) return;
  progress.value = (audio.value.currentTime / audio.value.duration) * 100;
  currentTime.value = formatTime(audio.value.currentTime);
};

const updateDuration = () => {
  if (!audio.value) return;
  duration.value = formatTime(audio.value.duration);
};

const handleEnded = () => {
  isPlaying.value = false;
  progress.value = 0;
  currentTime.value = '00:00';
};
</script>