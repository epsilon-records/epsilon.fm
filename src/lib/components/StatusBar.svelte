<script lang="ts">
	import FavouritesMenu from './FavouritesMenu.svelte';
	import SystemClock from './SystemClock.svelte';
	import NetworkStatus from './NetworkStatus.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
	import { statusBarVisible } from '$lib/stores/ui';
	import { currentTrack, isPlaying } from '$lib/stores/audio';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
	import { Badge } from '$lib/components/ui/badge';
</script>

{#if $statusBarVisible}
	<div class="fixed bottom-0 left-0 z-30 w-full bg-background">
		<div class="flex items-center justify-between p-1">
			<div class="flex items-center">
				<FavouritesMenu />{#if $currentTrack}
					<Badge variant={$isPlaying ? 'default' : 'secondary'}>
						{$isPlaying ? '⏸️ Now Playing:' : '▶️ Paused:'}
						{$currentTrack.title} - {$currentTrack.artist}
					</Badge>
				{/if}
			</div>
			<div class="flex items-center">
				<MadeWithLove />
			</div>
			<div class="flex items-center">
				<NetworkStatus />
				<SystemClock />
			</div>
		</div>
	</div>
{/if}
