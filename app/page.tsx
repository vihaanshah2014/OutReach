'use client'
import { useState } from 'react';
import Image from "next/image";
import { Instagram, Twitter, Youtube } from 'lucide-react';

export default function Home() {
  const [socialHandle, setSocialHandle] = useState('');
  const [socialData, setSocialData] = useState(null);

  const fetchSocialData = async () => {
    try {
      const response = await fetch('/api/magic', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ socialHandle }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      setSocialData(data);
    } catch (error) {
      console.error('Failed to fetch social data:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 p-8">
      <main className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">Social Dashboard</h1>
          <p className="text-gray-600 dark:text-gray-400">Track all social media content in one place</p>
        </div>

        {/* Input Form */}
        <div className="mb-8">
          <input
            type="text"
            value={socialHandle}
            onChange={(e) => setSocialHandle(e.target.value)}
            placeholder="Enter social media handle"
            className="p-2 border border-gray-300 rounded"
          />
          <button
            onClick={fetchSocialData}
            className="ml-4 p-2 bg-blue-500 text-white rounded"
          >
            Fetch Data
          </button>
        </div>

        {/* Social Stats */}
        {socialData && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm">
              <div className="flex items-center gap-3 mb-4">
                <Instagram size={24} />
                <h2 className="font-bold">{socialData.instagram.username}</h2>
              </div>
              <p className="text-2xl font-bold">{socialData.instagram.followers}</p>
              <p className="text-gray-600 dark:text-gray-400">Followers</p>
            </div>

            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm">
              <div className="flex items-center gap-3 mb-4">
                <Twitter size={24} />
                <h2 className="font-bold">{socialData.twitter.username}</h2>
              </div>
              <p className="text-2xl font-bold">{socialData.twitter.followers}</p>
              <p className="text-gray-600 dark:text-gray-400">Followers</p>
            </div>

            <div className="bg-white dark:bg-gray-800 p-6 rounded-lg shadow-sm">
              <div className="flex items-center gap-3 mb-4">
                <Youtube size={24} />
                <h2 className="font-bold">{socialData.youtube.username}</h2>
              </div>
              <p className="text-2xl font-bold">{socialData.youtube.subscribers}</p>
              <p className="text-gray-600 dark:text-gray-400">Subscribers</p>
            </div>
          </div>
        )}

        {/* Recent Content */}
        {socialData && (
          <div className="space-y-12">
            {/* Instagram Posts */}
            <section>
              <h2 className="text-2xl font-bold mb-6">Recent Instagram Posts</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {socialData.instagram.recentPosts.map((post) => (
                  <div key={post.id} className="bg-white dark:bg-gray-800 rounded-lg overflow-hidden">
                    <Image src={post.imageUrl} alt={post.caption} width={300} height={300} />
                    <div className="p-4">
                      <p className="text-sm text-gray-600 dark:text-gray-400">{post.caption}</p>
                      <p className="text-sm font-bold mt-2">{post.likes} likes</p>
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* Tweets */}
            <section>
              <h2 className="text-2xl font-bold mb-6">Recent Tweets</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {socialData.twitter.recentTweets.map((tweet) => (
                  <div key={tweet.id} className="bg-white dark:bg-gray-800 p-6 rounded-lg">
                    <p className="text-gray-800 dark:text-gray-200">{tweet.text}</p>
                    <div className="flex gap-4 mt-4 text-sm text-gray-600 dark:text-gray-400">
                      <span>{tweet.likes} likes</span>
                      <span>{tweet.retweets} retweets</span>
                    </div>
                  </div>
                ))}
              </div>
            </section>

            {/* YouTube Videos */}
            <section>
              <h2 className="text-2xl font-bold mb-6">Recent YouTube Videos</h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {socialData.youtube.recentVideos.map((video) => (
                  <div key={video.id} className="bg-white dark:bg-gray-800 rounded-lg overflow-hidden">
                    <Image src={video.thumbnail} alt={video.title} width={300} height={169} />
                    <div className="p-4">
                      <h3 className="font-bold mb-2">{video.title}</h3>
                      <p className="text-sm text-gray-600 dark:text-gray-400">{video.views} views</p>
                    </div>
                  </div>
                ))}
              </div>
            </section>
          </div>
        )}
      </main>
    </div>
  );
}
