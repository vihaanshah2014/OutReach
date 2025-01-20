import { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { socialHandle } = req.body;

    // Simulate fetching data based on the social handle
    const data = {
      instagram: {
        username: socialHandle,
        followers: "10.5K",
        recentPosts: [
          {
            id: 1,
            imageUrl: "https://placeholder.co/300x300",
            likes: "1.2K",
            caption: "Living my best life! #lifestyle",
          },
          {
            id: 2,
            imageUrl: "https://placeholder.co/300x300",
            likes: "890",
            caption: "Beautiful sunset 🌅",
          },
        ],
      },
      twitter: {
        username: socialHandle,
        followers: "5.2K",
        recentTweets: [
          {
            id: 1,
            text: "Just launched my new project! Check it out!",
            likes: "234",
            retweets: "45",
          },
          {
            id: 2,
            text: "Thanks everyone for the amazing support!",
            likes: "567",
            retweets: "89",
          },
        ],
      },
      youtube: {
        username: socialHandle,
        subscribers: "100K",
        recentVideos: [
          {
            id: 1,
            thumbnail: "https://placeholder.co/300x169",
            title: "How I Built My First App",
            views: "12K",
          },
          {
            id: 2,
            thumbnail: "https://placeholder.co/300x169",
            title: "Day in the Life Vlog",
            views: "8.5K",
          },
        ],
      },
    };

    res.status(200).json(data);
  } else {
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
