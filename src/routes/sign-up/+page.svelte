<script lang="ts">
	import SignUp from 'clerk-sveltekit/client/SignUp.svelte';
	import { mode } from 'mode-watcher';
	import { neobrutalism, dark } from '@clerk/themes';
</script>

<div class="m-4 self-center">
	<SignUp
		appearance={{ baseTheme: $mode === 'dark' ? dark : neobrutalism }}
		redirectUrl="/onboarding"
	/>
</div>
