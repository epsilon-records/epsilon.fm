<script lang="ts">
	import FavouritesMenu from './FavouritesMenu.svelte';
	import SystemClock from './SystemClock.svelte';
	import NetworkStatus from './NetworkStatus.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
	import { statusBarVisible, sidebarVisible } from '$lib/stores/ui';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
</script>

{#if $statusBarVisible}
	<SignedOut>
		<div class="status-bar fixed bottom-0 left-0 w-full" class:pl-14={$sidebarVisible}>
			<div class="flex items-center justify-between p-1">
				<div class="flex items-center"></div>
				<div class="flex items-center">
					<MadeWithLove />
				</div>
				<div class="flex items-center"></div>
			</div>
		</div>
	</SignedOut>
	<SignedIn>
		<div class="status-bar fixed bottom-0 left-0 z-30 w-full border-t bg-background">
			<div class="flex items-center justify-between p-1">
				<div class="flex items-center">
					<FavouritesMenu />
				</div>
				<div class="flex items-center">
					<SystemClock />
				</div>
				<div class="flex items-center">
					<NetworkStatus />
				</div>
			</div>
		</div>
	</SignedIn>
{/if}
