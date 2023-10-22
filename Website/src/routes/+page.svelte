<script>
// @ts-nocheck


	import { GradientButton } from "flowbite-svelte";

</script>
<!DOCTYPE html>
<!-- svelte-ignore a11y-missing-attribute -->
<html>
<head>

    <style>

        body {
            font-family:sans-serif;
        }

        header {
            background-color: #000;
            color: #fff;
            padding: 1rem;
        }

        h1, h2 {
            margin: 0;
        }

        h1 {
            font-size: 2rem;
        }

        h2 {
            font-size: 1.5rem;
        }

        main {
            padding: 1rem;
        }

        section {
            margin-bottom: 1rem;
        }

        h3 {
            font-size: 1.25rem;
        }

        p {
            font-size: 1rem;
        }

        ul {
            list-style-type: disc;
            margin-left: 1rem;
        }

        a {
            color: #000;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        footer {
            background-color: #000;
            color: #fff;
            padding: 1rem;
            text-align: center;
        }

        nav {
            background-color: #fff;
            border-bottom: 1px solid #ccc;
            padding: 1rem;
        }

        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }

        nav li {
            display: inline-block;
            margin-right: 1rem;
        }

        nav a {
            color: #000;
            text-decoration: none;
        }

        nav a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Patients</h1>
        <h2>Are you a patient looking for your patient portal?
        </h2>

        <script>
            import { GradientButton } from 'flowbite-svelte';
          </script>

<GradientButton color="pinkToOrange">Get Started</GradientButton>

    </header>

    <nav>
        <ul>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <li><a href="#">Home</a></li>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <li><a href="#">About</a></li>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <li><a href="#">How it works</a></li>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <li><a href="#">Benefits</a></li>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>

    <main>
        <section>
            <h3>Introducing Dr.Watch</h3>
            <p>Dr.Watch is a groundbreaking new tool that uses the Terra API to leverage standardized data from smartwatches for early detection of serious health issues. Our initial focus is on anomaly detection for impending Alzheimer's/dementia.</p>
        </section>
        <section>
            <h3>How it works</h3>
            <p>Dr.Watch collects data from your smartwatch and analyzes it for signs of anomalies. These anomalies can be indicative of early-stage Alzheimer's/dementia. If Dr.Watch detects any anomalies, it will alert you so that you can take action.</p>
        </section>
        <section>
            <h3>Benefits of Dr.Watch</h3>
            <ul>
                <li>Early detection of Alzheimer's/dementia</li>
                <li>Peace of mind knowing that you are being monitored for early signs of Alzheimer's/dementia</li>
                <li>The ability to take action if anomalies are detected</li>
            </ul>
        </section>
        <section>
            <h3>Get started today</h3>
            <p>Sign up for a free trial of Dr.Watch today and start taking control of your health.</p>
            <!-- svelte-ignore a11y-invalid-attribute -->
            <a href="#">Sign up for a free trial</a>
        </section>
    </main>

    <footer>
        &copy; 2023 Dr.Watch
    </footer>
</body>
</html>
