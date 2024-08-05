<script lang="ts">
	import PlusCircled from 'svelte-radix/PlusCircled.svelte';
	import AlbumArtwork from '$lib/components/album-artwork.svelte';
	import PodcastEmptyPlaceholder from '$lib/components/podcast-empty-placeholder.svelte';
	import { listenNowAlbums, madeForYouAlbums } from './(data)/albums';
	import { Button } from '$lib/components/ui/button';
	import { Separator } from '$lib/components/ui/separator';
	import * as Tabs from '$lib/components/ui/tabs';
	import { ScrollArea } from '$lib/components/ui/scroll-area';
	import { ArtistService } from '$lib/api/soundcharts/client/services.gen';

	let artistData = ArtistService.getApiV29ArtistByUuid({
		path: { uuid: '8fab7c54-0e0f-43a5-bf62-def4792d345a' }
	})
		.then((response) => response.data)
		.catch((error) => {
			console.error('Error fetching artist data:', error);
			return null;
		});
</script>

<Tabs.Root value="music" class="h-full space-y-6">
	<div class="space-between flex items-center">
		<Tabs.List>
			<Tabs.Trigger value="music" class="relative">Music</Tabs.Trigger>
			<Tabs.Trigger value="podcasts">Podcasts</Tabs.Trigger>
			<Tabs.Trigger value="live" disabled>Live</Tabs.Trigger>
		</Tabs.List>
		<div class="ml-auto mr-4">
			<Button>
				<PlusCircled class="mr-2 h-4 w-4" />
				Add music
			</Button>
		</div>
	</div>
	<Tabs.Content value="music" class="border-none p-0 outline-none">
		<div class="flex items-center justify-between">
			<div class="space-y-1">
				<h2 class="text-2xl font-semibold tracking-tight">Listen Now</h2>
				<p class="text-sm text-muted-foreground">Top picks for you. Updated daily.</p>
			</div>
		</div>
		<Separator class="my-4" />
		<div class="relative">
			<ScrollArea orientation="both">
				<div class="flex space-x-4 pb-4">
					{#each listenNowAlbums as album}
						<AlbumArtwork
							{album}
							class="w-[250px]"
							aspectRatio="portrait"
							width={250}
							height={330}
						/>
					{/each}
				</div>
			</ScrollArea>
		</div>
		<div class="mt-6 space-y-1">
			<h2 class="text-2xl font-semibold tracking-tight">Made for You</h2>
			<p class="text-sm text-muted-foreground">Your personal playlists. Updated daily.</p>
		</div>
		<Separator class="my-4" />
		<div class="relative">
			<ScrollArea orientation="both">
				<div class="flex space-x-4 pb-4">
					{#each madeForYouAlbums as album}
						<AlbumArtwork {album} class="w-[150px]" aspectRatio="square" width={150} height={150} />
					{/each}
				</div>
			</ScrollArea>
		</div>
	</Tabs.Content>
	<Tabs.Content value="podcasts" class="h-full flex-col border-none p-0 data-[state=active]:flex">
		<div class="flex items-center justify-between">
			<div class="space-y-1">
				<h2 class="text-2xl font-semibold tracking-tight">New Episodes</h2>
				<p class="text-sm text-muted-foreground">Your favorite podcasts. Updated daily.</p>
			</div>
		</div>
		<Separator class="my-4" />
		<PodcastEmptyPlaceholder />
	</Tabs.Content>
</Tabs.Root>
