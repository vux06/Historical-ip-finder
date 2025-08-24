<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Historical IP Finder</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            color: #333;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4b6cb7;
            color: #fff;
            padding: 2rem;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        main {
            padding: 2rem;
            max-width: 900px;
            margin: auto;
        }
        section {
            margin-bottom: 2rem;
        }
        h2 {
            color: #4b6cb7;
        }
        pre {
            background-color: #eaeaea;
            padding: 1rem;
            overflow-x: auto;
            border-radius: 5px;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
        }
        ul {
            list-style-type: square;
            padding-left: 1.2rem;
        }
        footer {
            text-align: center;
            padding: 1rem;
            color: #666;
            border-top: 1px solid #ddd;
            margin-top: 2rem;
        }
        a {
            color: #4b6cb7;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .badge {
            display: inline-block;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
        }
    </style>
</head>
<body>

<header>
    <h1>Historical IP Finder</h1>
    <p>Track historical A records for any domain using SecurityTrails API</p>
</header>

<main>
    <section>
        <h2>About</h2>
        <p>
            <strong>Historical IP Finder</strong> is a lightweight Python tool that allows security researchers,
            bug bounty hunters, and network analysts to fetch historical A records of domains. 
            Discover all IP addresses associated with a domain over time and understand its hosting changes.
        </p>
    </section>

    <section>
        <h2>Features</h2>
        <ul>
            <li>Query historical DNS A records for any domain.</li>
            <li>Output unique IP addresses in a clean format.</li>
            <li>Minimal dependencies, fast and easy to use.</li>
            <li>Integrates easily into recon or pentesting workflows.</li>
        </ul>
    </section>

    <section>
        <h2>Installation</h2>
        <pre><code>git clone https://github.com/yourusername/historical-ip-finder.git
cd historical-ip-finder
pip install -r requirements.txt</code></pre>
        <p>Make sure you have a valid SecurityTrails API key before running the tool.</p>
    </section>

    <section>
        <h2>Usage</h2>
        <pre><code>python historical_ip_finder.py -u example.com</code></pre>
        <p>Replace <code>example.com</code> with the target domain.</p>
    </section>

    <section>
        <h2>Dependencies</h2>
        <ul>
            <li>Python 3.x</li>
            <li><a href="https://pypi.org/project/requests/">requests</a></li>
            <li><a href="https://docs.python.org/3/library/argparse.html">argparse</a></li>
        </ul>
    </section>

    <section>
        <h2>License</h2>
        <p>MIT License &copy; 2025 Your Name. Feel free to use, modify, and share!</p>
    </section>
</main>

<footer>
    Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a>
</footer>

</body>
</html>
