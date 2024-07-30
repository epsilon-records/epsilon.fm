<script lang="ts">
	import * as Menubar from '$lib/components/ui/menubar/index.js';
</script>

<Menubar.Menu>
	<Menubar.Trigger class="hidden md:block">Account</Menubar.Trigger>
	<Menubar.Content>
		<Menubar.Group>
			<Menubar.Label inset>Switch Label</Menubar.Label>
			<Menubar.RadioGroup value="nieuwe-groove-collectief">
				<Menubar.RadioItem disabled value="epsilon-records">Epsilon Records</Menubar.RadioItem>
				<Menubar.RadioItem disabled value="nieuwe-groove-collectief"
					>Nieuwe Groove Collectief</Menubar.RadioItem
				>
				<Menubar.RadioItem disabled value="diverse-records">diVerse Records</Menubar.RadioItem>
			</Menubar.RadioGroup>
		</Menubar.Group>
		<Menubar.Separator />
		<Menubar.Group>
			<Menubar.Label inset>Switch Artist</Menubar.Label>
			<Menubar.RadioGroup value="vozz-rich">
				<Menubar.RadioItem disabled value="vozz-rich">Vozz Rich</Menubar.RadioItem>
			</Menubar.RadioGroup>
		</Menubar.Group>
		<Menubar.Separator />
		<Menubar.Item inset href="https://accounts.epsilon.fm/organization"
			>Manage Artist...</Menubar.Item
		>
		<Menubar.Item inset href="https://accounts.epsilon.fm/user">Manage Account...</Menubar.Item>
		<Menubar.Item inset href="https://billing.stripe.com/p/login/5kA5kRfnU4AP4s88ww"
			>Manage Billing...</Menubar.Item
		>
		<Menubar.Separator />
		<Menubar.Item inset href="https://accounts.epsilon.fm/create-organization"
			>Add Artist...</Menubar.Item
		>
	</Menubar.Content>
</Menubar.Menu>
