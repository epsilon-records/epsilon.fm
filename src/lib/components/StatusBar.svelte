<script lang="ts">
	import FavouritesMenu from './FavouritesMenu.svelte';
	import CurrentTime from './CurrentTime.svelte';
	import NetworkStatus from './NetworkStatus.svelte';
	import MadeWithLove from './MadeWithLove.svelte';
	import '$src/app.css';
	import { statusBarVisible, sidebarVisible } from '$lib/stores/ui';
	import SignedIn from 'clerk-sveltekit/client/SignedIn.svelte';
	import SignedOut from 'clerk-sveltekit/client/SignedOut.svelte';
</script>

{#if $statusBarVisible}
	<div class="status-bar fixed bottom-0 left-0 w-full border-t" class:pl-14={$sidebarVisible}>
		<div class="flex items-center justify-between p-1">
			<div class="flex items-center">
				<SignedIn><FavouritesMenu /></SignedIn>
			</div>
			<div class="flex items-center">
				<SignedOut>
					<MadeWithLove />
				</SignedOut>
				<SignedIn>
					<CurrentTime />
				</SignedIn>
			</div>
			<div class="flex items-center space-x-1">
				<SignedIn>
					<NetworkStatus />
				</SignedIn>
			</div>
		</div>
	</div>
{/if}
